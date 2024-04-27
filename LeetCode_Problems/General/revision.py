# palindrome number
# def palindrome(x: int):

#     original_val = x
#     reversed_val = 0

#     while x > 0:
#         # get the last digit
#         lst_digit = x % 10

#         # construct the reversed val

#         reversed_val = reversed_val * 10 + lst_digit

#         # divide x by floor division of 10 till x gets to zero

#         x = x // 10


#     return (original_val == reversed_val)


# num = 111
# result = palindrome(num)
# print(result)


# binary search
from typing import List


# def binary_search(nums: List[int], target) -> int:
#     # HELP ME GOD.

#     # handle edge case
#     if not nums or len(nums) < 0: return -1

#     # initialize pointers

#     left_ptr, right_ptr = 0, len(nums) - 1

#     while left_ptr <= right_ptr:
#         # determine the middle of the array

#         mid = (left_ptr + right_ptr) // 2

#         # check if the element is found in the  middle
#         if nums[mid] == target:
#             return f"found {nums[mid]} at index {mid}"
#         elif nums[mid] < target:
#             left_ptr = mid + 1
#         else:
#             right_ptr = mid - 1

#         print('this is left pointer', left_ptr)
#         print('this is right pointer', right_ptr)


#     return "not found"

# nums = [1, 2, 3, 5]
# result = binary_search(nums, 4)
# print(result)


# def roman_to_integer(numeral: str) -> int:
#     if len(numeral) < 0: return -1

#     roman_val = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

#     # variable to hold the result
#     res = 0

#     for i in range(len(numeral)):
#         if i + 1 < len(numeral) and roman_val[numeral[i]] < roman_val[numeral[i + 1]]:
#             # minus from the result
#             res -= roman_val[numeral[i]]
#         else:
#             # add to the result
#             res += roman_val[numeral[i]]

#     return res


# numeral = 'MCMXCIV'
# result = roman_to_integer(numeral)
# print(result)


# # best time to buy stock.
# def best_time_to_buy_stock(prices: List[int]) -> int:
#     if not prices or len(prices) < 0: return -1

#     buy = prices[0]
#     potential_profit = 0
#     max_profit = 0

#     for i in range(len(prices) - 1):
#         if prices[i] < buy:
#             buy = prices[i]

#         else:
#             potential_profit = prices[i + 1] - buy


#             if potential_profit > max_profit:
#                 max_profit = potential_profit

#             # max_profit = max(potential_profit, max_profit)


#     print('this is the buy', buy)
#     print('this is the potential profit',  potential_profit)

#     return max_profit


# days = [5, 1, 1, 1, 2]
# result = best_time_to_buy_stock(days)
# print(result)
