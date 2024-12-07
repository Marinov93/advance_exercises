from collections import deque

cups_capacity = deque([int(x) for x in input().split()])
bottles_capacity = deque([int(x) for x in input().split()])

wasted_water = 0

while cups_capacity and bottles_capacity:
    current_cup = cups_capacity.popleft()
    current_bottle = bottles_capacity.pop()

    if current_cup <= current_bottle:
        wasted_water += current_bottle - current_cup
    else:
        cups_capacity.appendleft(current_cup - current_bottle)

if cups_capacity:
    print(f"Cups:", *cups_capacity)
else:
    print(f"Bottles:", *bottles_capacity)

print(f"Wasted litters of water: {wasted_water}")