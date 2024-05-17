from typing import List
# """
# Problem: Search Insert Position.
# Description:
# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4
 

# Constraints:

# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums contains distinct values sorted in ascending order.
# -104 <= target <= 104
# """

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums or len(nums) <= 0:
            return 0
        
        # approach
        # would be using a binary search in order to implement an algo of O(log n) runtime complexity.

        u = len(nums) - 1
        l = 0

        while l <= u:
            # get the middle of the array
            middle = (l + u) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                # increase the upper bound
                u = middle - 1
            else:
                #  increase lower bound
                l = middle + 1

        return l
            

nums = [1, 3, 4, 7, 8, 9]
target = 5
# Output: 2
model = Solution()
result = model.searchInsert(nums, target)
print(result)
