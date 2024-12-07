my_stack = []

for el in range(int(input())):
    queries = input().split()
    command = queries[0]
    my_stack.reverse()
    if command == '1':
        my_stack.append((queries[1]))
    elif command == '2':
        if my_stack:
            my_stack.pop()
    elif command == '3':
        if my_stack:
            max_number = max(my_stack)
            print(max_number)
    elif command == '4':
        if my_stack:
            min_number = min(my_stack)
            print(min_number)

my_stack.reverse()
print(*my_stack, sep=', ')
