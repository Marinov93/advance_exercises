parking_lot = set()

for _ in range(int(input())):
    direction, car_number = input().split(", ")

    if direction == 'IN':
        parking_lot.add(car_number)
    else:
        parking_lot.remove(car_number)

if parking_lot:
    print(*parking_lot, sep='\n')
else:
    print("Parking Lot is Empty")