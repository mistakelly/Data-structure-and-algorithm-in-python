from typing import List

# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:

#         if not strs:
#             return ""

#         prefix = ""

#         for i in range(len(strs[0])):

#             for j in range(1, len(strs)):

#                 if i == len(strs[j]) or strs[0][i] != strs[j][i]:
#                     return prefix
                
#             prefix += strs[0][i]
                

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ptr  = 1
        for i in range(1, len(nums) - 1):

            if nums[i] != nums[i + 1]:

                nums[ptr] = nums[i + 1]

                ptr += 1

        print(nums)

        return ptr

nums = [1,1,2]
model = Solution()
result = model.removeDuplicates(nums)

print(result)