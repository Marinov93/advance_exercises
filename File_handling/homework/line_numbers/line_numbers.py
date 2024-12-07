from string import punctuation

with open("text.txt", "r") as input_file:
    data = input_file.readlines()

output_file = open("output.txt", "w")

for line in range(len(data)):
    letters = 0
    symbols = 0
    for symbol in data[line]:
        if symbol.isalpha():
            letters += 1
        elif symbol in punctuation:
            symbols += 1

    output_file.write(f"Line {line + 1}: {data[line][:-1]} ({letters})({symbols})\n")

output_file.close()

