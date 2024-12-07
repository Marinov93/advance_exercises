from collections import deque

quantity_food = int(input())
orders_of_food = deque([int(x) for x in input().split()])
max_order = max(orders_of_food)
print(max_order)

while orders_of_food:
    if quantity_food >= orders_of_food[0]:
        removed_order = orders_of_food.popleft()
        quantity_food -= removed_order
    else:
        break
if not orders_of_food:
    print("Orders complete")
else:
    print(f"Orders left: {' '.join([str(order) for order in orders_of_food])}")




