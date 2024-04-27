class Solution:
    def isPalindrome(self, s: str) -> bool:
        # HELP ME GOD.
        refined_str, palindrome = "", ""
        reversed_str = "".join(reversed(s))
        for i in range(len(s)):
            if s[i].isalnum():
                refined_str += s[i].lower()

            if reversed_str[i].isalnum():
                palindrome += reversed_str[i].lower()

        return palindrome == refined_str


palindrome = "A man, a plan, a canal: Panama"
model = Solution()
result = model.isPalindrome(palindrome)
print(result)


6710875612