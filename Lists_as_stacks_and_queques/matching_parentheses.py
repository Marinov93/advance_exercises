text = input()
stack = []

for element in range(len(text)):
    if text[element] == "(":
        stack.append(element)
    elif text[element] == ")":
        closing_parentheses = stack.pop()
        print(text[closing_parentheses:element + 1])