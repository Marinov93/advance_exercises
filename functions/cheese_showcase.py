def sorting_cheeses(**kwargs):
    final_result = ''
    result = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))
    for cheese, quantity in result:
        final_result += f"{cheese}\n"
        result = sorted(quantity, reverse=True)
        final_result += f"\n".join([str(x) for x in result]) + "\n"
    return final_result



print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
