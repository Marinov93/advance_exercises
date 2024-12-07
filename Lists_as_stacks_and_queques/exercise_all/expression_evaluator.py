from collections import deque
# input from console with data

expression = input().split()

queue = deque()
# Logic

for el in expression:
    if el not in '+-*/':
        queue.append(int(el))
    else:
        while len(queue) > 1:
            num_1 = queue.popleft()
            num_2 = queue.popleft()
            if el == '+':
                queue.appendleft(num_1 + num_2)
            elif el == '-':
                queue.appendleft(num_1 - num_2)
            elif el == '*':
                queue.appendleft(num_1 * num_2)
            elif el == '/':
                queue.appendleft(num_1 // num_2)

print(queue.popleft())
