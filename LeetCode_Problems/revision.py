from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        print('nums', nums)

        tmp_dic = {}
        for i, val in enumerate(nums):
            complement = target - val

            print('i', i)
            print('complement', complement)


            print(tmp_dic)
            if complement in tmp_dic:
                return tmp_dic[complement], i
            

            
            
            tmp_dic[val] = i
          



    


result = Solution()
print(result.twoSum([2, 5, 5, 5, 11], 10))

