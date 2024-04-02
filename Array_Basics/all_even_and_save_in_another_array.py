# Python program to store all even numbers from an array in another array
def even_element(lst):
    """
    :param lst:
    :return:  even list []
    """
    even_lst = []
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            even_lst.append(lst[i])
    return even_lst


even_list = even_element([1, 3, 4, 8, 6, 7])
print(even_list)
