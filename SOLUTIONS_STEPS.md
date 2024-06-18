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

## Problem 3: Best time to buy and sell stock (Easy)
**steps** 
1. initialize a buy and profit variables.
2. Buy at first day eg == (buy = prices[0])
3. Loop through array starting from day 1, since we already bought at day 0.
4. Compare if any day price is lesser than initial bought price.
5. if price is lower
   * Rebuy on that day.
6. else
   * compare the potential_profit with the original profit, if potential profit is greater than original profit, update profit variable and finally return profit. 
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


# LINKED LIST
## Problem 1: Remove Duplicate (Easy).
**steps** 
1. Initialize a head pointer and a tmp pointer, both set to None.
2. Loop through the list while tmp and tmp.next are not None:
   *This ensures you’re not trying to access properties of a None object.
3. Inside the loop, check if tmp.data is equal to tmp.next.data:
   *This identifies duplicate nodes.
4. If a duplicate is found:
   *Update tmp.next to point to tmp.next.next. This effectively removes the duplicate node from the list by bypassing it.
5. If no duplicate is found:
   *Move tmp to the next node by setting tmp = tmp.next. This advances to the next node in the list.
6. Continue the loop until all nodes are processed.


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

