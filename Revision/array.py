from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        # HELP ME GOD


        start = 0
        end = len(s) - 1


        while start < end:
            tmp = s[start]
            s[start] = s[end]
            s[end] = tmp
            end -= 1
            start += 1

        return s
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # HELP ME GOD

        if not nums:
            return None

       
        tmp_dic = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            
            if diff in tmp_dic:
                return tmp_dic[diff], i
            tmp_dic[nums[i]] = i

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # HELP ME GOD

        answer = []

        for i in range(len(nums)):
            product = 1
            print('nums[i]', nums[i])
            for j in range(len(nums)):
                if i != j:
                    product *= nums[j]
                    
            answer.append(product)

        return answer

        



    

s = ["h","e","l","l","o"]
model = Solution()

# REVERSE STRING 
reverse_str = model.reverseString(s)
# print(reverse_str)

# TWO SUM
arr = [2,7,11,15]
target = 9
two_sum = model.twoSum(arr, target)
# print(two_sum)

# PRODUCT EXCEPT SELF
product = model.productExceptSelf([1,2,3,4])
print(product)