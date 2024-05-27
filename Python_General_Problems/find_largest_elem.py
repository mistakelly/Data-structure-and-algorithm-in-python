# first method.
# def find_largest_elem(lst):
#     """
#         program that finds the largest element of an array.
#     :param lst:
#     :return: int
#     :time complexity  = O(n) linear time.
#     """
#     lst_size = len(lst)
#     largest_elem = 0
#
#     for i in range(lst_size):
#         if lst[i] > largest_elem:
#             largest_elem = lst[i]
#
#     return largest_elem
#
# result = find_largest_elem([1,3,4,8,6,7])
# print(result)

# second method

def find_largest_elem(lst):
    """
    :param lst:
    :return:  int or float
    time complexity == the sorted method makes use of O(n log n)
                        while the actual search uses O(1) constant time.
    """
    lst = sorted(lst, reverse=True)
    return lst[0]


result = find_largest_elem([1, 3, 4, 8, 6, 7])
print(result)




