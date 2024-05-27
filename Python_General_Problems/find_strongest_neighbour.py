#Given an array arr[] of N positive integers. The task is to find the maximum
# for every adjacent pair in the array.

"""
Examples:
Input: 1 2 2 3 4 5
Output: 2 2 3 4 5

Input: 5 5
Output:5
 """


def find_strongest_neighbour(arr):
    arr_size = len(arr)
    max_arr = []

    for i in range(arr_size):
        # return
        if arr[i] > arr[i] + 1:
            max_arr.append(arr[i])
        else:
            max_arr.append(arr[i])
    return max_arr


result = find_strongest_neighbour([1, 2, 2, 3, 4, 5])
print(result)
