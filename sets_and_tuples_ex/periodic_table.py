elements = set()

for i in range(int(input())):
    for element in input().split():
        elements.add(element)

print(*elements, sep='\n')