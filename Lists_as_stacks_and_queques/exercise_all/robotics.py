from collections import deque
from datetime import datetime, timedelta

robots = {}

# Input the robots data
for n in input().split(";"):
    name, time_needed = n.split("-")  # ROB-15 -> name = ROB, time_needed = 15
    robots[name] = [int(time_needed), 0]  # [time needed, time left to finish task]

# Input the start time of the factory
factory_time = datetime.strptime(input(), "%H:%M:%S")

# Initialize the products queue
products = deque()

# Reading products
while True:
    product = input()
    if product == 'End':
        break
    products.append(product)

# Main loop to assign products to robots
while products:
    factory_time += timedelta(seconds=1)  # Time advances by 1 second
    product = products.popleft()

    # Update each robot's remaining working time
    for name, value in robots.items():
        if value[1] > 0:
            robots[name][1] -= 1

    # Find a free robot
    free_robot = None
    for name, value in robots.items():
        if value[1] == 0:  # This robot is free
            free_robot = name
            break

    # If no free robot, requeue the product and continue
    if free_robot is None:
        products.append(product)
        continue

    # Assign the product to the free robot
    robots[free_robot][1] = robots[free_robot][0]  # Reset the working time
    print(f"{free_robot} - {product} [{factory_time.strftime('%H:%M:%S')}]")
