from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # HELP ME GOD.

        new_set = set()


        for i in range(len(nums)):
            if nums[i] not in new_set:
                new_set.add(nums[i])
            else:
                new_set.remove(nums[i])


        return new_set.pop()



num = [4,1,2,1,2]
model = Solution()
result = model.singleNumber(num)
print(result)