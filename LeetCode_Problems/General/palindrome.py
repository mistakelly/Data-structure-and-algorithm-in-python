# 9. Palindrome Number
# Given an integer x, return true if x is a  palindrome and false otherwise.

# Example 1:
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        
        original_x = x
        reversed_x = 0

        while x > 0:

            # get the last digit of x by doing a modules division of x by 10

            last_digit = x % 10

            # construct the reversed digit

            reversed_x = reversed_x * 10 + last_digit

            # break down x till it gets to zero, by doing a floor division with 10.

            x = x // 10

        # compare original_x with reversed_x

        return (original_x == reversed_x)


palindrome = 121
model = Solution()
result = model.isPalindrome(palindrome)
print(result)