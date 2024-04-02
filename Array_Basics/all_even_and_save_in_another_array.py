# Python program to store all even numbers from an array in another array
# def even_element(lst):
#     even_lst = []
#     for i in range(len(lst)):
#         if lst[i] % 2 == 0:
#             even_lst.append(lst[i])
#     return even_lst
#
#
# even_list = even_element([1, 3, 4, 8, 6, 7])
# print(even_list)


def get_middle(lst):
    sorted_array = sorted(lst)
    leng = len(sorted_array)
    middle_list = leng / 2

    print(sorted_array[middle_list])


even_list = get_middle([1, 3, 4, 8, 6, 7, 8])
# print(even_list)
