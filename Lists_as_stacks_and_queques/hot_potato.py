from collections import deque

kids_names = deque(input().split())
toss = int(input())

while len(kids_names) > 1:
    for el in range(toss - 1):
        kid = kids_names.popleft()
        kids_names.append(kid)
    print(f"Removed {kids_names.popleft()}")

print(f"Last is {kids_names.popleft()}")