# numbers = input().split("|")
#
# my_list = []
#
# for x in numbers[::-1]:
#     my_list.extend(x.split())
#
# print(*my_list)


numbers = [text.split() for text in input().split("|")]
print(*[' '.join(my_list) for my_list in numbers[::-1] if my_list])