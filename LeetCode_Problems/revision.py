# # from typing import List


# # class Solution:
# #     def twoSum(self, nums: List[int], target: int) -> List[int]:
# #         print('nums', nums)

# #         tmp_dic = {}
# #         for i, val in enumerate(nums):
# #             complement = target - val

# #             print('i', i)
# #             print('complement', complement)


# #             print(tmp_dic)
# #             if complement in tmp_dic:
# #                 return tmp_dic[complement], i
# #             tmp_dic[val] = i

# # result = Solution()
# # # print(result.twoSum([2, 5, 5, 5, 11], 10))

# # class Solution:
# #     def isPalindrome(self, s: str) -> bool:
# #         join_words = "".join(alph.lower() for alph in s if alph.isalnum())
# #         reversed_words = "".join(alph.lower() for alph in s[::-1] if alph.isalnum())

# #         print('reversed_words', reversed_words)


# #         for i in range(len(reversed_words)):
# #             if (join_words[i] != reversed_words[i]):
# #                 return False
            

# #         return True
# #         #     if (join_words[i] != )
# #         #     print(val.isalnum())
# #         #     # print(f'i: {i} val: {val}')
# #         print('joinwords', join_words)



# # # s = "A man, a plan, a canal: Panama"

# # # print('s === ', s[::-1])
# # # import re
# # # polish_word = re.sub('[^a-zA-Z0-9]', '', s).lower()

# # # print('is true', polish_word == polish_word[::-1])

# # # print('polish_word', polish_word)
# # # p = "AmanaplanacanalPanama"
# # # result = Solution()
# # # print(result.isPalindrome(s))

# # str1 = 'kelly'
# # str2 = 'kelly'

# # # print(str1 == str2)

# # class Solution:
# #     def maxProfit(self, prices: List[int]) -> int:

# #         buy = prices[0]
# #         profit = 0

# #         for i in range(len(prices) -1):

# #             if prices[i] < buy:
# #                 buy = prices[i]
            
# #             sell = prices[i + 1] - buy

# #             if (sell > profit):
# #                 profit = sell

# #         return profit
    
# # result = Solution()
# # # print(result.maxProfit([7,1,5,3,6,4]))


# # def reverse_arr(arr):
# #     print('normal arr', arr)
# #     start = 0
# #     end = len(arr) - 1

# #     while start < end:
# #         tmp = arr[start]

# #         arr[start] = arr[end]
# #         arr[end] = tmp

# #         start += 1
# #         end -= 1

# #     return arr



# # # print('reversed arr', reverse_arr([7,1,5,3,6,4]))


# # # python slicing

# # string = 'I am going to school'

# # def longest_prefix(arr):
# #     prefix = ""
# #     for s in arr[0]:
# #         print('s', s)
# #         for k in arr[1:]:
# #             print('k', k)

# #             for l in k:
# #                 print('s', s)
# #                 print('l', l)
# #                 if s == l:
# #                     prefix += s
                
# #                 # prefix += l
# #     return prefix



# # arr = ["flower", "flow","flight"]
# # # print('longest prefix', longest_prefix(arr))



# # # sliced_list = [1, 2, 3, 4, 5]

# # # answer = 'a gn'

# # # print('slicing', sliced_list[1:])


# # # matrix = [
# # #     [1, 2, 3],     # Row 0
# # #     [4, 5, 6],     # Row 1
# # #     [7, 8, 9]      # Row 2
# # # ]



# # # for row in matrix:
# # #     print('row', row)
# # #     for col in row:
# # #         print('col', col)



# # # for i in range(len(matrix)):
# # #     # print(f'row: <{i}>', matrix[i])
# # #     for j in range(len(matrix[i])):
# # #         print(f"Element at ({i}, {j}) is {matrix[i][j]}")

# # # you are given a 2D array (matrix) like this:


# # # matrix = [
# # #     [1, 2],
# # #     [3, 4]
# # # ]


# # # sum = 0
# # # for i in range(len(matrix)):
# # #     for j in range(len(matrix[i])):
# # #         sum += matrix[i][j]

# # # print('sum', sum)

# # # 👉 Task:
# # # Write code that counts how many numbers in the matrix are greater than 2.

# # matrix = [
# #     [2, 5, 1],
# #     [4, 0, 3]
# # ]
# # def num_greater_than_2(matrix):
# #     count = 0
# #     for i in range(len(matrix)):
# #         for j in range(len(matrix[i])):
# #             if matrix[i][j] > 2:
# #                 count += 1
# #     return count

# # # result = num_greater_than_2(matrix)
# # # print('result', result)


# # matrix = [
# #     [12, 7, 9],
# #     [5, 15, 8],
# #     [3, 10, 6]
# # ]

# # # 🧊 Matrix Problem 2: Find the Maximum Element

# # def find_largest_num(matrix):
# #     max_elem = matrix[0][0]
# #     for i in range(len(matrix)):
# #         for j in range(len(matrix[i])):
# #             if matrix[i][j] > max_elem:
# #                 max_elem = matrix[i][j]

# #     return max_elem


# # result = find_largest_num(matrix)
# # # print('result', result)





# # # Matrix Problem 3: Sum of Each Row
# # def sum_of_each_matrix_row(matrix):
# #     rows = [0] * len(matrix)
# #     print('rows length', len(rows))
# #     for i in range(len(matrix)):
# #         sum_of_rows = 0
# #         for j in range(len(matrix[i])):
# #             sum_of_rows += matrix[i][j]
# #         rows[i] = sum_of_rows


    
# #     return '\n'.join(f'sum of row {i} is {row}' for i, row in enumerate(rows))




# # matrix = [
# #     [3, 4, 5],
# #     [1, 2, 3],
# #     [7, 8, 9]
# # ]


# # # result = sum_of_each_matrix_row(matrix)
# # # print(result)




# # prefix_array = ["flowwrish", "flow", "flowwrish"]


# # def find_longest_prefix(words:str) -> str:
# #     prefix = ""

# #     for i in range(len(words[0])):
# #         for j in range(1, len(words)):
# #             if i >= len(words[j]) or words[0][i] != words[j][i]:
# #                 return prefix

# #         prefix += words[0][i]

# #     return prefix


# # result = find_longest_prefix(prefix_array)
# # # print('longest prefix', result)


# # nums = [1, 2, 3, 4, 5, 6]

# # # answer is 5
# # # buy at day 1 sell at day 6
# # def best_time_to_buy_stock(nums):

# #     buy = nums[0]
# #     profit = 0

# #     for i in range(len(nums) -1):
# #         print('nums[i]', i)
# #         if nums[i] < buy:
# #             buy = nums[i]


    

# #         potential_profit = nums[i + 1] - buy

# #         if potential_profit > profit:

# #             profit = potential_profit

# #     return profit
    
    



# # # result = best_time_to_buy_stock(nums)
# # # print(f'profit == ({result})')





# # word = "cup is going to school"

# # import re
# # def palindrome_string(word: str) -> str:


# #     polished_word = re.sub('[^a-zA-Z0-9]', '', word).lower()
# #     print(polished_word[::-3])

# #     return polished_word == polished_word[::-1]


# # # result = palindrome_string(word)
# # # print('result', result)


# # # duplicate = 

# # # import time


# # # def find_dup(nums):
# # #     tmp = {}

# # #     for i in range(len(nums)):
# # #         if  nums[i] in tmp:
# # #             print('nums[i]', tmp[nums[i]])
# # #             return True
        
# # #         tmp[nums[i]] = i
        

# # #     return False
# # #         # print(nums[i])

# # # start_time = time.time()
# # # print(find_dup(duplicate))
# # # end_time = time.time()

# # # print("Execution time:", end_time - start_time, "seconds")


# # # # for arrary tmp it took 
# # # # False
# # # # Execution time: 34.11207294464111 seconds



# # # # using dictionary
# # # #  python3 revision.py
# # # # longest prefix flow
# # # # nums[i] 100000
# # # # True
# # # # Execution time: 0.007093906402587891 seconds
# # # # kellys-MacBook-Pro:LeetCode_Problems mac$


# # # two_sum_arr = [1, 2, 3, 2, 5]
# # # target = 6

# # # def best_time_to_buy_stock(nums):
# # #     buy = nums[0]
# # #     profiit = 0


# # #     for i in range(len(nums) -1):
# # #         if nums[i] < buy:
# # #             buy = nums[i]

# # #         potential_profit = nums[i + 1] - buy


# # #         if potential_profit > profiit:
# # #             profiit = potential_profit

# # #         print(f'buy: {buy} sell: {potential_profit}')


# # #     return profiit


# # # result = best_time_to_buy_stock(two_sum_arr)
# # # print('result == ', result)




# # def longest_prefix(word: str):
# #     """
# #         initiialize prefix
# #         loop through the first word.
# #         loop throuh from the second word
# #         if i is equal to or greater than the len of each word in the arrary, then if the arrary[j][i] != arr[0][i]
# #             return prefix
# #         prefix += word[0][i]
# #     """


# #     prefix = ""

# #     for i in range(len(word[0])):
# #         for j in range(1, len(word)):
# #             print('word', word[j][i])
# #             if i >= len(word[j]) or word[j][i] != word[0][i]:
# #                 return prefix
            
# #         prefix += word[0][i]

# #     return prefix



# # words = ['flow', 'flower', 'flows']

# # result = longest_prefix(words)
# # print('result', result)


# # out of context 😏.
# #       3. should we look into us restructuring our app from host and invited guest scope
# #            to maybe 🤔 an event type of app where our main purpose is to allow people share 
# #             their memories in an event ?? i'm just saying this to make our app open and you know 
# #              allow for more users and users retention.



# word = "A man, a plan, a canal: Panama"
# fix_word = ''.join(word)
# polished_word = ""




# for i in range(len(word) -1, -1, -1):
#     if word[i].isalnum():
#         polished_word += word[i].lower()

#     if word[i].isalnum():
#         fix_word += word[i].lower()


# print(fix_word == polished_word)


# print('polished_word', polished_word)



# def custom_join(word: str, delimeter):
#     join_word = ""

#     for i in range(len(word)):
#         join_word += f'{delimeter}{word}'

#     return joined_word




# sample_word = "A man, a plan, a canal: Panama"

# joined_word = custom_join(sample_word, ' ')
# print('joined word', joined_word)

# class Solution(object):
#     def isPalindrome(self, s):

#         string_only = filter(int., s)

#         print(list(string_only))

#         # word = ''.join(string_only)

#         # print(word)

#         # print('string', string_only)

#         # for char in s:
#         #     if char.isalnum():
#         #         cleaned_str = ''.join(char.lower())
    
#         # return cleaned_str == cleaned_str[::-1]


# sample_word = "A man, a plan, a canal: Panama"

# result = Solution()
# print(result.isPalindrome(sample_word))



from typing import List


def reverse_arr(arr):
    start, end = 0, len(arr) - 1

    while start < end:
        tmp = arr[start]
        arr[start] = arr[end]
        arr[end] = tmp

        #  increase pointers
        start += 1
        end -= 1

    return arr

arr = [1, 2, 3, 4, 5]
# print('normal', arr)

result = reverse_arr(arr)
# print('reveresed', result)

nums = [1,2,3,1]

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        return len(set(nums)) == len(nums)
        print(set(nums))



result = Solution().containsDuplicate(nums)

# print('result', result)


       



import re
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            print('haystack', haystack[i: len(needle)])
            if haystack[i : len(needle)] == needle:
                return i

        return -1

haystack = "butsadsad"
needle = "sad"


# print(haystack[0: 1000])

# print(haystack == needle)

# haystack , needle = "hello",  "ll"

# result = Solution().strStr(haystack, needle)
# print('result', result)

# print(haystack == needle)


# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         prefix_result = [1] * len(nums)
#         prefix = 1



#         for i in range(len(nums)):
#             prefix_result[i] = prefix
#             prefix *= nums[i]
#         print('prefix_result', prefix_result)
           
# nums = [1, 2, 3, 4]
# result = Solution().productExceptSelf(nums)
# print('result', result)


# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         tmp_arr = list(s)

#         print('s', s)
#         print('tpm', tmp_arr)
#         for i in range(len(s)):
#            if s[i] not in (s[i + 1: i + len(tmp_arr)]):
#             return i

#         return -1


# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         # tmp_arr = list(s)

#         dict = {}

#         print('s', s)
#         # print('tpm', tmp_arr)
#         for i in range(len(s)):
#             dict[s[i]] = 1 if s[i] not in dict else dict[s[i]] + 1


        
#         print('dict', dict)
#             # return i

#         for i in range(len(s)):
#             if (dict[s[i]] == 1):
#                 return i


#         return -1 
      


# word = "l e etcode"
# word =  "loveleetcode"
# word = "aabb"
# result = Solution().firstUniqChar(word)
# print('firstunique', result)


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_of_left_self = 1
        left_result = [1] * len(nums)

        for i in range(len(nums)):
            left_result[i] = product_of_left_self
            product_of_left_self *= nums[i]


        product_of_right_self = 1
        right_result = [1] * len(nums)

        for i in range(len(nums) - 1, - 1,  -1):
            right_result[i] = product_of_right_self
            product_of_right_self *= nums[i]

        result = [1] * len(nums)
        product_of_arr_except_self = 1
        for i in range(len(nums)):
           product_of_arr_except_self = left_result[i] * right_result[i]
           result[i] = product_of_arr_except_self
        

        print('result', left_result)
        print('right result', right_result)
        return result


nums = [1,2,3,4]
# result = Solution().productExceptSelf(nums)
# print('product_of_array', result)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        """
        loop through `t` 
            if t[i] not in s:
                return false
            return true
        """

        if len(t) != len(s):
            return False


        s_dict = {}
        t_dict = {}


        for i in range(len(s)):
            if s[i] not in s_dict:
                s_dict[s[i]] = 1
            else:
                s_dict[s[i]] =  s_dict[s[i]] + 1

            if t[i] not in t_dict:
                 t_dict[t[i]] = 1
            else:
                 t_dict[t[i]] =  t_dict[t[i]] + 1

        for key, value in s_dict.items():       
            if t_dict[key] != value:
                return False
           

        return True
        

      

s = "acca"
t = "accc"
# result = Solution().isAnagram(s, t)

# print('anagram', result)


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -999999999999999999
        potential_sum = 0 


        print('max sum', max_sum)
        
        
        for i in range(len(nums)):
            potential_sum = 0 
            for j in range(i, len(nums)):
                potential_sum +=  nums[j]

                # print('potential_sum', potential_sum)
    
                if potential_sum > max_sum:
                    max_sum = potential_sum
    
        return max_sum if max_sum > potential_sum else potential_sum
        return max_sum



        
              


# nums = [-2,1,-3,4,-1,2,1,-5,4]
# nums = [1,2,3,4,5,6,7,8,9,10]
# nums = [5,4,-1,7,8]
# nums = [-2,1,-3,4,-1,2,1,-5,4]
nums  = [-1]
# result = Solution().maxSubArray(nums)
# print('max-array', result)


nums = []
min_value = float('inf')

for num in nums:
    if num < min_value:
        min_value = num

# print(min_value)  # Still inf, but is that meaningful? 🤔

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        tmp_s = {}
        tmp_t = {}

        for i in range(len(s)):
            if s[i] not in tmp_s:
                tmp_s[s[i]] = 1
            else:
                tmp_s[s[i]] =  tmp_s[s[i]]  + 1

            print('tmp_s', tmp_s)


            tmp_t[t[i]] = tmp_t.get(t[i], 0) + 1

        # print('tmp_s', tmp_s.items())
        # print('tmp_t', tmp_t)

        for key in tmp_s:
            print('key', tmp_s[key])
            if tmp_s.get(key, 0) != tmp_t.get(key, 0):
                return False


        return True
    
s = "rat"
t = "car"
# result = Solution().isAnagram(s, t)
# print('isAnagram', result)



class Solution:
      def strStr(self, haystack: str, needle: str) -> int:

        print('cup' in 'bocuPsok')

        if needle not in haystack:
            return -1


haystack = "sadbutsad"
needle = "sad"
# result = Solution().strStr(haystack, needle)
# print('needle in haystack', result) 



class Practice:
    def test(self, nums):
        i = 0
        while nums[i] != 0:
            print('i', nums[i])
            i+= 1

nums = [1, 2, 3, 4, 5, 0, 0, 0]
# result = Practice().tes t(nums)
# print('test', result)



class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        if n == 0:
            return nums1

        if m == 0:
            return nums2

        ptr_1, ptr_2 = 0, 0
        i = 0
        tmp_arr = [0] * len(nums1)
        

        for i in range(len(nums1)) :
            if nums1[ptr_1] <= nums2[ptr_2] and nums1[ptr_1] != 0:
                tmp_arr[i] = nums1[ptr_1]
                ptr_1 +=1
            else:
                tmp_arr[i] = nums2[ptr_2]
                ptr_2 +=1
            i+=1
        print('tmp_array', tmp_arr)
                

nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 5]
m = 3
n = 3
# result = Solution().merge(nums1,  m, nums2, n)
# print('tmp_arr', result) 

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[m + n -1] = nums1[m-1]
                m -= 1
            else:
                nums1[m + n -1] = nums2[n-1]
                n -= 1
        

        if n > 0:
            nums1[:n] = nums2[:n]





class Solution:
    def reverseWords(self, s: str) -> str:
        print('s', s)
        tmp_list = list(s)
        print('tmp_list', tmp_list)
        
        
        start = 0
        for i in range(len(tmp_list)):
            end = i - 1
            if tmp_list[i] == ' ':
                print('yes')
                while start <= end: 
                    tmp_list[start], tmp_list[end] = tmp_list[end], tmp_list[start]
                    start += 1
                    end -= 1

                start = i + 1

        end = len(tmp_list) - 1
        while start <= end:
            tmp_list[start], tmp_list[end] = tmp_list[end], tmp_list[start]
            start += 1
            end -= 1


        print('tmp_Arr', tmp_list)

        s = ''.join(tmp_list)

        return s


# s = "Let's take LeetCode contest"
# result = Solution().reverseWords(s)
# print('reverse string III', result)

# "s'teL ekat edoCteeL tsetnoc"

# s'teL ekat  edoCteeL   contest
# # 's', "'", 't', 'e', 'L',


def REL_func(word):
    count = 1
    tmp_list = []

    for i in range(len(word) - 1):
        if word[i] == word[i +  1]:
            count += 1
        else:
            tmp_tuple = count, word[i]
            tmp_list.append(tmp_tuple)
            count = 1
    return tmp_list
        


word = 'AAABBBCCCDDDE'

result = REL_func(word)
print('word', result) 