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
# print(result.twoSum([2, 5, 5, 5, 11], 10))

class Solution:
    def isPalindrome(self, s: str) -> bool:
        join_words = "".join(alph.lower() for alph in s if alph.isalnum())
        reversed_words = "".join(alph.lower() for alph in s[::-1] if alph.isalnum())

        print('reversed_words', reversed_words)


        for i in range(len(reversed_words)):
            if (join_words[i] != reversed_words[i]):
                return False
            

        return True
        #     if (join_words[i] != )
        #     print(val.isalnum())
        #     # print(f'i: {i} val: {val}')
        print('joinwords', join_words)



# s = "A man, a plan, a canal: Panama"

# print('s === ', s[::-1])
# import re
# polish_word = re.sub('[^a-zA-Z0-9]', '', s).lower()

# print('is true', polish_word == polish_word[::-1])

# print('polish_word', polish_word)
# p = "AmanaplanacanalPanama"
# result = Solution()
# print(result.isPalindrome(s))

str1 = 'kelly'
str2 = 'kelly'

# print(str1 == str2)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy = prices[0]
        profit = 0

        for i in range(len(prices) -1):

            if prices[i] < buy:
                buy = prices[i]
            
            sell = prices[i + 1] - buy

            if (sell > profit):
                profit = sell

        return profit
    
result = Solution()
# print(result.maxProfit([7,1,5,3,6,4]))


def reverse_arr(arr):
    print('normal arr', arr)
    start = 0
    end = len(arr) - 1

    while start < end:
        tmp = arr[start]

        arr[start] = arr[end]
        arr[end] = tmp

        start += 1
        end -= 1

    return arr



print('reversed arr', reverse_arr([7,1,5,3,6,4]))