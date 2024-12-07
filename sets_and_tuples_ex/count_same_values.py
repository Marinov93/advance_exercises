numbers = tuple(map(float, input().split()))

occurrences = {}

for num in numbers:
    if num not in occurrences:
        occurrences[num] = 0
    occurrences[num] += 1

[print(f"{key} - {value} times") for key, value in occurrences.items()]
