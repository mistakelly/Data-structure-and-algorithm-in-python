# Reversing a List in Python

def reverse_list(arr):
    size = len(arr)
    start = 0
    end = size - 1

    while start < end:
        tmp = arr[start]
        arr[start] = arr[end]
        arr[end] = tmp
        start += 1
        end -= 1

    return arr


values = reverse_list([1, 2, 3, 4, 5, 6])
print(values)
# output == [5, 4, 3, 2, 1]
