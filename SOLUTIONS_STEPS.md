# ARRAY PROBLEMS []
## Problem 1: Two Sum (Easy)
**Steps:**
1. Used a hash map to store the indices of the elements.
2. Checked if the complement of the current element exists in the hash map.
3. Returned the indices of the two elements that add up to the target sum.

## Problem 2: Remove Element (Easy)
**steps** 
1. Identified the problem as removing all occurrences of a given value.
2. Decided to use a two-pointer approach for efficiency.
3. Avoided using `pop()` to reduce time complexity.
4. Tested the solution with various edge cases.


# GENERAL PROBLEMS
## Problem 1: Palindrome Number (Easy)
**steps** 
1. Saved the initial value of `num` for comparison.
2. Initialized `reversed_num` to 0.
3. Started a loop while `num > 0`.
4. Extracted the last digit of `num` using `num % 10`.
5. Updated `reversed_num` to `reversed_num * 10 + last_digit`.
6. Removed the last digit from `num` using integer division (`num //= 10`).
7. Compared the original number with `reversed_num` to determine if it is a palindrome.


