class Solution:
    def romanToInt(self, s: str) -> int:
        if not s:
            return None

        tmp_dic ={
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0

        for i in range(len(s) - 1):
            if tmp_dic[s[i]] < tmp_dic[s[i + 1]]:
                total -= tmp_dic[s[i]]
            else:
                total += tmp_dic[s[i]]

        # after everything add the last value of x to total cause our loop stoped  one digit before the last digit (len(s) - 1)
        total += tmp_dic[s[-1]]

        return total


model = Solution()
s = 'III'
s = "MCMXCIV"
roman_to_int = model.romanToInt(s)
print(roman_to_int)