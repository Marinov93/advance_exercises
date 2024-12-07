from collections import deque

chocolates = [int(x) for x in input().split(", ")]
cups_milk = deque([int(y) for y in input().split(", ")])

milkshakes = 0

# LOGIC

while chocolates and cups_milk and milkshakes < 5:
    if chocolates[-1] <= 0:
        chocolates.pop()
        continue
    if cups_milk[0] <= 0:
        cups_milk.popleft()
        continue

    if chocolates[-1] == cups_milk[0]:
        milkshakes += 1
        chocolates.pop()
        cups_milk.popleft()
    else:
        cups_milk.rotate(-1)
        chocolates[-1] -= 5

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

print(f'Chocolate: {", ".join([str(n) for n in chocolates]) if chocolates else "empty"}')
print(f'Milk: {", ".join([str(x) for x in cups_milk]) if cups_milk else "empty"}')
