# Given a list in Python and provided the positions of the elements,
# write a program to swap the two elements in the list.
"""
    Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
    Output : [19, 65, 23, 90]
"""


def swapPositions(lst, pos1, pos2):
    size = len(lst)
    if pos1 <= 0 or pos2 <= 0:
        return "sorry position must start from 1"
    if pos1 > size or pos2 > size:
        return f"Sorry positions are out of the list index list (list size {size})"
    if pos1 == pos2:
        return f"Positions are the same, no swapping needed"

    tmp = lst[pos1 - 1]
    lst[pos1 - 1] = lst[pos2 - 1]
    lst[pos2 - 1] = tmp

    return lst


numbers = [23, 65, 19, 90, 42, 56, 71, 5, 33, 78,
           12, 88, 29, 50, 10, 47, 62, 3, 85, 15,
           37, 69, 24, 81, 8, 45, 60, 17, 95, 28]

values = swapPositions(numbers, 3, 3)
print(values)

