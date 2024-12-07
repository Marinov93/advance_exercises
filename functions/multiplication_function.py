def multiply(*args) -> int:
    a = 1
    for el in args:
        a *= el
    return a



print(multiply(1, 4, 5))
print(multiply(4, 5, 6, 1, 3))
print(multiply(2, 0, 1000, 5000))
