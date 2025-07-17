# 3Sum
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

# The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]

# Output: [[-1,-1,2],[-1,0,1]]
# Explanation:
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].

# Example 2:

# Input: nums = [0,1,1]

# Output: []
# Explanation: The only possible triplet does not sum up to 0.

# Example 3:

# Input: nums = [0,0,0]

# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.

# Constraints:

# 3 <= nums.length <= 1000
# -10^5 <= nums[i] <= 10^5


# Solution:
from typing import List

# The most naive solution that I came up with is to use a nested loop and check every combination of three numbers (BRUTE FORCE)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Ofcourse there is a brute force method where you over the list 3 times and find the combinations
        temp = set()
        nums.sort()
        # Here we sort the array first so that we can avoid duplicates as in different patterns of the same triplet
        # Now we can use a nested loop to find the triplets 
        # We use a set to avoid duplicates
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        temp.add(tuple([nums[i], nums[j], nums[k]]))
        result = []
        for i in temp:
            result.append(i)
        return result