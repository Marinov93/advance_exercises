from collections import deque

green_light_time = int(input())
free_windows_time = int(input())

traffic = 0


while True:
    command = input()
    if command == 'END':
        break
    car_name = command
    for el in car_name:
        letters_going = car_name.count(car_name)
        print(letters_going)