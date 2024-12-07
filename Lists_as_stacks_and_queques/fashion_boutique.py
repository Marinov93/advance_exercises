clothes = [int(x) for x in input().split()]
rack_space = int(input())

rack_counter = 1
current_rack_space = rack_space

while clothes:
    cloth = clothes.pop()

    if current_rack_space >= cloth:
        current_rack_space -= cloth
    else:
        rack_counter += 1
        current_rack_space = rack_space - cloth

print(rack_counter)