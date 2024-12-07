from collections import deque

available_water = int(input())

people = deque()

while True:
    action = input()
    if action == 'Start':
        break
    else:
        people.append(action)

while True:
    command = input()
    if command == 'End':
        break
    elif command.startswith('refill'):
        refill = int(command.split()[1])
        available_water += refill
    else:
        needed_litres = int(command)
        if needed_litres <= available_water:
            person = people.popleft()
            available_water -= needed_litres
            print(f"{person} got water")
        else:
            person = people.popleft()
            print(f"{person} must wait")
print(f"{available_water} liters left")

print(*people)
