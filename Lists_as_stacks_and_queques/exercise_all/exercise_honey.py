from collections import deque

# input from console with data needed

working_bees = deque([int(x) for x in input().split()])
nectar = [int(y) for y in input().split()]
symbols = deque(input().split())

# logic for problem

made_honey = 0

while working_bees and nectar:
    bee = working_bees.popleft()
    nectar_counter = nectar.pop()
    if bee > nectar_counter:
        working_bees.appendleft(bee)
        continue
    else:
        curr_symbol = symbols.popleft()
        if curr_symbol == '+':
            made_honey += abs(bee + nectar_counter)
        elif curr_symbol == '-':
            made_honey += abs(bee - nectar_counter)
        elif curr_symbol == '*':
            made_honey += abs(bee * nectar_counter)
        elif curr_symbol == "/":
            if nectar_counter == 0:
                continue
            else:
                current_honey = bee / nectar_counter
                made_honey += current_honey

print(f"Total honey made: {made_honey}")
if working_bees:
    print(f"Bees left: {', '.join([str(x) for x in working_bees])}")
if nectar:
    print(f"Nectar left: {', '.join([str(x) for x in nectar])}")
