# Two Integer Sum II
# Solved 
# Given an array of integers numbers that is sorted in non-decreasing order.

# Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2. Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.

# There will always be exactly one valid solution.

# Your solution must use 
# O
# (
# 1
# )
# O(1) additional space.

# Example 1:

# Input: numbers = [1,2,3,4], target = 3

# Output: [1,2]
# Explanation:
# The sum of 1 and 2 is 3. Since we are assuming a 1-indexed array, index1 = 1, index2 = 2. We return [1, 2].

# Constraints:

# 2 <= numbers.length <= 1000
# -1000 <= numbers[i] <= 1000
# -1000 <= target <= 1000


# Solution:

# The most naive soluation that I came up with is to use a nested loop and check every combination of two numbers (BRUTE FORCE)
from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            for j in range(i+ 1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i + 1,j + 1]


# Binary Search Solution:
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Lets implement binary search. 
        # So the idea here is you loop through every number and find the deficit i.e. target - current number
        # And you find that deficit using binary search from i + 1 and len(array)

        # So Lets code this solution
        for i in range(len(numbers)):
            deficit = target - numbers[i]
            l, r = i + 1, len(numbers) - 1
            while l <= r:
                mid = (l + r)// 2
                if deficit == numbers[mid]:
                    return [i + 1, mid + 1]
                if numbers[mid] > deficit:
                    r = mid - 1
                else:
                    l = mid + 1
        return []
    


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Okay now the most efficient solution that meets all the requirements
        # Two pointer solution where there ofcourse two pointers, 
        # First we point front pointer to the start of the list and back pointer to the end of the list
        # Add those numbers at that position and see the difference
        # If the difference is 0 then we found our indices 
        # If the target is smaller than the sum we found then move the right pointer one to the left
        # And if the target is bigger than the sum we found then move the left pointer one to the right until we find our two magic numbers
        
        # Looking at the previous solution, it looks like this solution is combination of binary search and two pointer which avoids having the store something in the hashmap

        fp = 0
        bp = len(numbers) - 1
        while fp < bp:
            cur_sum = numbers[fp] + numbers[bp]
            if cur_sum == target:
                return [fp + 1, bp + 1]
            elif cur_sum > target:
                bp -= 1
            else:
                fp += 1
        return []




