def grocery_store(**kwargs):
    kwargs = sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

    result = []

    for product, quantity in kwargs:
        result.append(f"{product}: {quantity}")

    return "\n".join(result)

print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))

