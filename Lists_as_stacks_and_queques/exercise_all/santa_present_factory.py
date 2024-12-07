from collections import deque

# Input with needed data -> materials and magic

materials = [int(x) for x in input().split()]
magic_levels = deque([int(x) for x in input().split()])

# list with crafted presents
crafted = []

# dict with given values of presents
presents = {150: "Doll", 250: "Wooden train", 300: "Teddy bear", 400: "Bicycle"}

# looping till we have materials and magic to craft

while materials and magic_levels:
    material_item = materials.pop() if magic_levels[0] or not materials[-1] else 0
    magic = magic_levels.popleft() if material_item or not magic_levels[0] else 0

    magic_counter = material_item * magic

    if presents.get(magic_counter):
        crafted.append(presents[magic_counter])
    elif magic_counter < 0:  # checking if operation is negative number
        materials.append(magic + material_item)
    elif magic_counter > 0:
        materials.append(material_item + 15)

if {"Doll", "Wooden train"}.issubset(crafted) or {"Teddy bear", "Bicycle"}.issubset(crafted):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    reversed_items = reversed(materials)
    materials_two = ", ".join(map(str, reversed_items))
    print(f"Materials left: {materials_two}")
if magic_levels:
    magic_stamina = ", ".join(map(str, magic_levels))
    print(f"Magic left: {magic_stamina}")

[print(f"{toy}: {crafted.count(toy)}") for toy in sorted(set(crafted))]