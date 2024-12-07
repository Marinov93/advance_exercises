# symbols = ("-", ",", ".", "!", "?")
#
# with open("text.txt", "r") as even_lines_file:
#     for i, j in enumerate(even_lines_file):
#         if i % 2 == 0:
#             for el in symbols:
#                 j = j.replace(el, "@")
#             print(" ".join(reversed(j.split())))

symbols = ("-", ",", ".", "!", "?")

with open("text.txt", "r") as file:
    text = file.readlines()

for lines in range(0, (len(text)), 2):
    for symbol in symbols:
        text[lines] = text[lines].replace(symbol, "@")

    print(*text[lines].split()[::-1])
