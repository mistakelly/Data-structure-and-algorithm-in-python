def find_target_O_log_n(arr, target):
    l = 0
    u = len(arr) - 1

    while l <= u:

        mid = (l + u) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            l = mid + 1
        else:
            u = mid - 1

    return l



# Example usage:
my_array = [1, 2, 3, 4, 5, 6]
mid = find_target_O_log_n(my_array, 4)
print(mid)
