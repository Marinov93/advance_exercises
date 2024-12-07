#Your task is to find the pairs of numbers whose sum equals the target number.

numbers = list(map(int, input().split()))
target_number = int(input())
#
# for num in range(len(numbers)):
#     if numbers[num] == '':
#         continue
#     for dig in range(num + 1, len(numbers)):
#         if numbers[dig] == '':
#             continue
#         if numbers[num] + numbers[dig] == target_number:
#             print(f"{numbers[num]} + {numbers[dig]} = {target_number}")
#             numbers[num] = ''
#             numbers[dig] = ''
#             break

target = set()
value_map = {}

for value in numbers:
    resulting_number = target_number - value
    target.add(resulting_number)
    value_map[resulting_number] = value
    if value in target:
        target.remove(value)
        pair = value_map[value]
        del value_map[value]
        print(f"{pair} + {value} = {target_number}")
    else:
        resulting_number = target_number - value
        target.add(resulting_number)
        value_map[resulting_number] = value