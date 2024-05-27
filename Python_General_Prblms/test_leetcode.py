from typing import List


def removeDuplicates(nums: List[int]) -> int:
        unique_arr = []
        k = 0

        for i in range(len(nums)):
            # for j in range(i + 1, len(nums)):
            if nums[i] not in unique_arr:
                unique_arr.append(nums[i])

        for j in unique_arr:
            nums[j] = unique_arr[j]
            k += 1

        return k


removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])

