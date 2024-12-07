def func_executor(*function_data):
    result = []

    for fun, args in function_data:
        result.append(f"{fun.__name__} - {fun(*args)}")

    return "\n".join(result)


def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


print(func_executor(
    (sum_numbers, (1, 2)),
    (multiply_numbers, (2, 4))
))
