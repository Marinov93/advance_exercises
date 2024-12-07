from collections import deque
customers = deque()
command = input()
while command != 'End':
    if command == 'Paid':
        print('\n'.join(customers))
        while customers:
            customers.popleft()
    elif command != 'Paid':
        customers.append(command)
    command = input()
print(f"{len(customers)} people remaining.")