from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        # HELP ME GOD.
        if not n:  return -1

        answer = []

        for i in range(1 ,n + 1):

            if i % 3 == 0 and i % 5 == 0:
                answer.append('FizzBuzz')
            elif i % 3 == 0:
                answer.append('Fizz')
            elif i % 5 == 0:
                answer.append('Buzz')
            else:
                answer.append(i)

        return answer




num = 15
model = Solution()
result = model.fizzBuzz(num)
print(result)