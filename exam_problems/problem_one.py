from collections import deque

packages = [int(el) for el in input().split()]
couriers = deque([int(el) for el in input().split()])

while packages and couriers:
    current_package = packages[-1]
    current_courier = couriers[0]

    if current_courier >= current_package:
        pass