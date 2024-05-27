"""
Question: Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        # HELP ME GOD
        if not s or len(s) <= 0:
            return 
        
        tmp_dic = {
            '(': ')',
            '[' : ']',
            '{' : '}'
        }

        print(value)

        for i in range(0, len(s), 2):
            for k, v in tmp_dic.items():
                if s[i] == k and s[i + 1] != v:
                    return False
           
        return True



# value  = "()"
# value = "()[]{}"
value = "(]"
model = Solution()
result = model.isValid(value)
print(result)
