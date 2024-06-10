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

---

# STRINGS PROBLEMS
## Problem 1: Roman to Integer (Medium)
**Steps:**
1. Initialized `total` to 0 and `prev_val` to 0.
2. Loop through the Roman numeral string in reversed order.
3. For each character, converted it to its corresponding integer value (`current_val`).
4. Compared `current_val` with `prev_val`:
   - If `current_val` is less than `prev_val`, subtracted `current_val` from `total`.
   - Otherwise, added `current_val` to `total`.
5. Updated `prev_val` to `current_val` for the next iteration.

## Problem 2: Longest Common Prefix (Easy)
**Steps:**
1. Initialized `prefix` as an empty string.
2. Loop through each character index of the first string (`strs[0]`).
3. For each index, loop through all strings in the list:
   - **Check if the current index exceeds the length of the current string** or if the character at the current index in `strs[0]` does not match the corresponding character in any other string.
   - **If either condition is true**, return the current `prefix`.
4. **If all strings match the current character index**, append the character to `prefix`.
5. Return the final `prefix` after processing all characters.

---


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

---

