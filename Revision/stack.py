# Write a function in python that can reverse a string using stack data structure. Use Stack class from the tutorial.

# def reverse_string(string):
#     # HELP ME GOD

#     reverse_str = ""
# # 
#     stack = []


#     for i in string:
#         stack.append(i)


#     while stack:
#         reverse_str += stack.pop()


#     return reverse_str


# string = "We will conquere COVID-19"


# result = reverse_string(string)

# print(result)

class Solution:
    def isValid(self, s: str) -> bool:
        # HELP ME GOD.
        # if s[0] == ('}') or s[0] == ']' or s[0] == ')':
        #     return False
            
            
        # stack = []
        
        # for char in s:
        #     if char == "{":
        #         stack.append('}')
        #     elif char == "(":
        #         stack.append(")")
        #     elif char == "[":
        #         stack.append("]")
        #     else:
        #         if not stack or char != stack.pop():
        #             print('this is char inside', char)
        #             print('inside here')
        #             return False
        # print(stack)

        # return True if not stack else False

        stack = []

        tmp_dic = {'(': ')', '[': ']', '{': '}'}


        for char in s:
            if char in tmp_dic:
                stack.append(tmp_dic[char])
            else:
                if not stack or stack.pop() != char:
                    return False
                
        return True if not stack else False
                





# s = "([()])"
s = '(()'
s = "]"
s = "(){}()"
s = "()[]{}(" 

model = Solution()

result = model.isValid(s)

print(result)

# print('}' == '{')

# output = "91-DIVOC ereuqnoc lliw eW"




