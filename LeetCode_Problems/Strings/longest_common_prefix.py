
from typing import List
"""
 Question: Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 
Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Initialize the prefix as an empty string
        prefix = ""
        
        # Outer loop: Iterate over each character index of the first string
        for i in range(len(strs[0])):
            # Inner loop: Iterate over each string in the list
            for j in range(len(strs)):
                # Check if the current index exceeds the length of the current string
                # or if the characters do not match
                if i == len(strs[j]) or strs[0][i] != strs[j][i]:
                    return prefix  # Return the current prefix if conditions are met
            
            # Add the current character to the prefix
            prefix += strs[0][i]
        
        # Return the final prefix after checking all characters
        return prefix

words = ["flower","flow","flight"]
model = Solution()
result = model.removeElement(words)
print(result)



# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         # initialize empty array

#         # not efficient for negative numbers,
#         # it places negative numbers at the end of the list, it was meant to be in front
#         # new_set = set(nums)
#         # tmp = list(new_set)
#         # count = len(new_set)

#         # nums.clear()

#         # for i in tmp:
#         #     nums.append(i)
#         # return count
        
#         unique = 1
#         count = 1
#         for i in range(len(nums) - 1):
#             if nums[i] != nums[i + 1]:
#                 nums[unique] = nums[i + 1]
#                 count += 1
#                 unique += 1

#         return count
# # 