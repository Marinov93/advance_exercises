odd_set = set()
even_set = set()

number = int(input())

for index in range(1, number + 1):
    letters = input()
    sum_asci = sum((ord(x) for x in letters)) // index

    if sum_asci % 2 == 0:
        even_set.add(sum_asci)
    else:
        odd_set.add(sum_asci)

sum_of_odd_set, sum_of_even_set = sum(odd_set), sum(even_set)

if sum_of_even_set == sum_of_odd_set:
    print(*odd_set.union(even_set), sep=', ')
elif sum_of_odd_set > sum_of_even_set:
    print(*odd_set.difference(even_set), sep=', ')
else:
    print(*odd_set.symmetric_difference(even_set), sep=', ')
