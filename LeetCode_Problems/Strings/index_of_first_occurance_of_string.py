class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        # Help Me GOD
        if not haystack: return -1

        for i in range(len(haystack)):
            print(haystack[i: i + len(needle)])
                # return i

        return -1
    
haystack = "sadbutsad"
needle = "sad"
model = Solution()
result = model.strStr(haystack, needle)
print(result)