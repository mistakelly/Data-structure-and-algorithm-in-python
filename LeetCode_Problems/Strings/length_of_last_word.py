"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal 
substring
 consisting of non-space characters only.

EXAMPLES.
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.

"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # HELP ME GOD.

        if not s:
            return -1
        
        # first solution.

        # split the string by spaces then get the length of the last word.
        # length = 0
        # curent_length = 0
        # for i in range(len(s)):
        #     if s[i] != ' ':
        #         curent_length += 1
        #     else:
        #         if curent_length > 0:
        #             length = curent_length
        #         curent_length = 0

        
        # if curent_length > 0:
        #     length = curent_length

        # return length

        # second_solution

        # i = len(s) - 1
        # length = 0

        # # move i to be exactly at the last character, ignoring the spaces.
        # while i > 0 and s[i] == ' ':
        #     i -= 1


        # # iterate from the end of the strings. and stop just immediately you encounter a space.
        # while i >= 0 and s[i] != ' ':
        #     length += 1
        #     i -= 1

        # return length

        # third solution.
        # using built in methods.

        last_word = len(s.split()[-1])

        return last_word





last_word = "luffy is still joyboyoooo"
model = Solution()
result = model.lengthOfLastWord(last_word)
print(result)
