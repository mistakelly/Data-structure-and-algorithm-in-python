from typing import List
"""
PROBLEM: Two Sum

Description
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:
2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
"""

# solution

def twoSum(nums: List[int], target: int) -> List[int]:
    # HELP ME GOD.

    # check for empty list
    if not nums or len(nums) <= 0:
        return 0

    # Not efficient enough
    # for i in range(len(nums) - 1):
    #     # iterate and compare at i with i + 1
    #     if nums[i] + nums[i + 1] == target:
    #         return [i, i + 1]
        
    # let's try another aproach
    left_operand = 0
    right_operand = 0

    # not the best solution, will improve when I learn bout Hashmap Datastructure.
    for i in range (len(nums)):
        for j in range(i, len(nums)):
            if nums[i] + nums[j] == target:
                left_operand = i
                right_operand = i + 1
        
    return [left_operand, right_operand]


arr2 = [2,7, 3, 11,15]
target = 10
result = twoSum(arr2, target)
print(result)
        
