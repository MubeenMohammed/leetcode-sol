

# Longest Consecutive Sequence
# Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

# A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.

# You must write an algorithm that runs in O(n) time.

# Example 1:

# Input: nums = [2,20,4,10,3,4,5]

# Output: 4
# Explanation: The longest consecutive sequence is [2, 3, 4, 5].

# Example 2:

# Input: nums = [0,3,2,5,4,6,1,1]

# Output: 7
# Constraints:

# 0 <= nums.length <= 1000
# -10^9 <= nums[i] <= 10^9



# Solution:
from typing import List

# Solution is brute force but we are avoid going through the array multiple times as we are checking if the current number is the start of the sequence
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # So the idea is to convert the array into a set and then iterate through the array
        # We are now trying to find different sequence length and every sequence has a starting point
        # So we go through the array and see if the current number is the start of the sequence or not
        # How do we check that? we do num - 1 not in set (finding if there any numbers in the sequence left of the current number )
        # If it is the start of the sequence then do while loop and find the sequence length
        # If its not the start of the sequence then skip the number
        # Finally find the length of longest sequence

        # Lets write the code for this above solution
        # Convert the array into a set
        my_set = set(nums)
        longest = 0
        for i in nums:
            length = 0
            if i - 1 not in my_set:
                cur = i
                length = 1
                while cur + 1 in my_set:
                    length += 1
                    cur += 1
                longest = max(longest, length) 
        return longest
    
# Solution using a different approach: brute force
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # First thought went to brute force where you look at each number and check their longest sequest starting with their number
        # Finally storing the max of longest length and current length
        my_set = set(nums)
        longest = 0
        if (len(nums)) == 0:
            return 0
        for i in range(len(nums)):
            cur, length = nums[i], 1
            while cur + 1 in my_set:
                length += 1
                cur = cur + 1
            longest = max(longest,length)
        return longest


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Sorting Solution

        # First sort the array
        nums.sort()
        if len(nums) == 0:
            return 0
        count = 0
        temp = 1
        for i in range(len(nums)):
            if i < len(nums) - 1:
                if nums[i] == nums[i + 1]:
                    continue
                if nums[i + 1] == nums[i] + 1:
                    temp += 1
                else:
                    temp = 1
            count = max(temp,count) 

        return count