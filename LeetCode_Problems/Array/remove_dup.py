from typing import List
""" Problem:  Remove Duplicates from Sorted Array
Description:
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.


Example 1:
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
 

Constraints:
1 <= nums.length <= 3 * 104
-100 <= nums[i] <= 100
nums is sorted in non-decreasing order.
"""


"""
    Thought process: 🤔
        The problem stated that the array is sorted in Non decreasing order
        Meaning that its simply in increasing order eg: 1, 1, 2, 3 ....

        so having that in mind 🤔.
        Do you know what i did ??
        
        unique_elem = 1
        I said ok, let me initialize unique elements to start at [1]
        reason to that is that since the elements, that means the lowest element is
        always going to start at the index 0 of the array, so we only have to start our swap from index 1 ok.

        count = 1

        why i initialized count to 1 ? 

        the reason to that is because we are to return the count of the unique element right ?? 

        so if that is the case ?

        that means that if we start our count at zero it will not include the first element at index 0 as unique element cause we only incremented count inside the if condition, so that is why i started count at index 0, so we can count the first element as unique element.


        Then inside the loop is where stuffs starts getting interesting. 💃🏽

        I iterated from length of nums till nums -1 which is just before the last element in the array right ??

        reason to that is because we are comparing nums[i] vs nums[i + 1]

        so if i don't stop at just before the last element, when the array reaches the last element, and we comparing nums[i] vs nums[i + 1] it will result to 
        IndexError: list index out of range

        cause the iterator nums[i] stoped at the last index of the array and yet we are comparing nums[i] vs nums[i + 1] which will result to exception.

        if nums[i] != nums[i + 1] ?

        this logic is very straight forward to the core.

        what i am checking is that since they are unique I only want to iterate till I found any element that is not unique
        
        once found ?

        I simply call the nums []  and pass the unique_elem as the index of the array and swap the values in there with the value of nums[i + 1] once swapped, I increase the value of the unique_element, eg: unique_elem += 1, so that the unique_elem would be at the next element of the nums after swap, so if i should find anther value that is not unique it would definitely be the number after the last element cause they are sorted then I swap again still maintaining the nums position.

        eg == arr = [1,1,2, 3, 3, 4]

        first iteration: nums[i] == nums[i + 1]
            skip
            
        i is increased to 1
        second iteration: nums[i] != nums[i + 1]

            then i swap nums[unique_elem] = nums[i + 1]
              nums[unique_elem] = 1, nums[i + 1] is == 2,
            which means we now have arr = [1, 2, 2, 3, 3, 4]

            unique_elem is increased to 2.
            unique_elem += 1
            count += 1

        third iteration:
            i is increased to 2
            third iteration:  nums[i] != nums[i + 1]

            then i swap nums[unique_elem] = nums[i + 1]
              nums[unique_elem] = 2, nums[i + 1] is == 3,
            which means we now have arr = [1, 2, 3, 3, 3, 4]
            count += 1
            unique_elem += 1



        fourth iteration:
            i is increased to 3
            nums[i] == nums[i + 1] 
            skip

        fifth iteration:
            i is increased to 4
            fifth iteration:  nums[i] != nums[i + 1]

            then i swap nums[unique_elem] = nums[i + 1]
              nums[unique_elem] = 3, nums[i + 1] is == 4,
            which means we now have arr = [1, 2, 3, 4, 3, 4]
            count += 1
            unique_elem += 1

        
        at this instance we are now at the element just before the last element.

        so we stop our iteration and return count .

        our array should look like this now:


            arr = [1, 2, 3, 4, 3, 4]
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # HELP ME GOD.
        # initialize empty array

        # not efficient for negative numbers, it places negative numbers at the end of the list, it was meant to be in front
        # new_set = set(nums)
        # tmp = list(new_set)
        # count = len(new_set)

        # nums.clear()

        # for i in tmp:
        #     nums.append(i)
        # return count

        # More Efficient to the previous solution.
        unique_elem = 1
        count = 1
        for i in range(len(nums) -1 ):
            if nums[i] != nums[i + 1]:
                nums[unique_elem] = nums[i + 1]
                count += 1
                unique_elem += 1

        print(nums)
        return count
        
arr = [1,1,2, 3, 3, 4]
# expected_arr =  [1, 2, 3, 4, 3, 4]
result = Solution()
answer = result.removeDuplicates(arr)
print(answer)

