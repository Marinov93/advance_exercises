number_x = set([int(x) for x in input().split()])
number_y = set([int(y) for y in input().split()])

for _ in range(int(input())):
    action = input().split()
    command = f'{action[0]} {action[1]}'
    numbers = [int(num) for num in action[2:]]
    if command == 'Add First':
        number_x.update(numbers)
    elif command == 'Add Second':
        number_y.update(numbers)
    elif command == 'Remove First':
        number_x.difference_update(numbers)
    elif command == 'Remove Second':
        number_y.difference_update(numbers)
    else:
        print(number_y.issubset(number_x) or number_x.issubset(number_y))

print(*sorted(number_x), sep=", ")
print(*sorted(number_y), sep=", ")
