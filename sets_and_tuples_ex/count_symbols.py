text = input()

for element in sorted(set(text)):
    print(f"{element}: {text.count(element)} time/s")