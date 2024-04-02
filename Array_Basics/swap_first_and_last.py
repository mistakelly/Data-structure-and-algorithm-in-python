# Given a list, write a Python program to swap first and last element of the list.

def swap_first_and_last(lst):
    size = len(lst)
    first = 0
    last = size - 1
    tmp = lst[first]
    lst[first] = lst[last]
    lst[last] = tmp
    return lst


values = swap_first_and_last([1, 2, 3, 4, 5])
print(values)

