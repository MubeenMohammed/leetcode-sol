# Contains Duplicate
# Solved 
# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

# Example 1:

# Input: nums = [1, 2, 3, 3]

# Output: true

# Example 2:

# Input: nums = [1, 2, 3, 4]

# Output: false



# Solution
# Very simple solution where you just store each value in the dictonary and for each subsequent value, you check if its already present in the dict
# If it is then return TRUE orelse return False


# COMPLEXITY
# O(n)


from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mem = {}
        for i in nums:
            if i in mem:
                return True
            else:
                mem[i] = 0
        return False