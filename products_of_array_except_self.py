# Products of Array Except Self
# Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

# Each product is guaranteed to fit in a 32-bit integer.

# Follow-up: Could you solve it in 
# O
# (
# n
# )
# O(n) time without using the division operation?

# Example 1:

# Input: nums = [1,2,4,6]

# Output: [48,24,12,8]
# Example 2:

# Input: nums = [-1,0,1,2,3]

# Output: [0,-6,0,0,0]
# Constraints:

# 2 <= nums.length <= 1000
# -20 <= nums[i] <= 20


# Solution:

# My firt thought was to first multiple all the elements and then divide the total by each element to get the result.
# But if there is a zero in the array, then the division will not work. since we cannot divide by zero. so we need to have a product of all the elements except the zero.
# There could also be multiple zeros in the array then the result will be all zeros.

from typing import List

# This solution is really simple as it multiples all the elements except the one at the current index.
# This is a brute force solution with O(n^2) time complexity.

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            prod = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                prod = prod * nums[j]
            result.append(prod)
        return result
        


# This solution is better as it has O(n) time complexity and O(1) space complexity. Division method

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zero_count = 1, 0
        # Get the product without considering zeros and also count number of zeros too
        result = []
        for i in nums:
            if i == 0:
                zero_count += 1
            else:
                prod = prod * i
        # If the zero count is more than 1 then solution is list of all zeros
        if zero_count > 1:
            return [0] * len(nums)
        
        # last two cases
        # Case 1: there is one zero: As you previously calculated the product without any zero, that is answer for result array with that zero index and for the rest of indices in the result is 0 as they multiply with 0
        # Case 2: There is no zeros -- This is simple as you have full prod just divide the prod with the current 
        # index value and add it to the result array
        
        for i,v in enumerate(nums):
            if zero_count == 1:
                if v == 0:
                    result.append(prod)
                else:
                    result.append(0)
            else:
                result.append(int(prod / v))

        return result
    

# This solution is better as it has O(n) time complexity and O(n) space complexity. No division method. Its prefix and postfix solution. although it is optimal in terms of time complexity, it uses extra space for prefix and postfix arrays.


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # There is a challenge to complete this problem without using division
        # So we will use prefix and postfix  which is two arrays for each of the operation where it calculates 
        # the product of all the values before that index
        # For example the input is [1,2,4,6] so 
        # prefix for this will be [1, 1, 2, 8]
        # Similary for postfix it is the same thing but from the opposite side
        # Postfix for the above example will be [48,24,6,1]
        # Now to get the output all we need is to multiply both arrays values at their respective indices
        # Output is [48,24,12,8]
        # Lets write the code for this solution

        result = []
        prefix = []
        postfix = [0] * len(nums)
        preprod = 1
        for i in range(len(nums)):
            prefix.append(preprod)
            preprod = preprod * nums[i]
        postprod = 1
        for i in range(len(nums) - 1, -1, -1):
            postfix[i] = postprod
            postprod = postprod * nums[i]
        for i in range(len(nums)):
            result.append(prefix[i] * postfix[i])

        return result
    

# This solution is better as it has O(n) time complexity and O(1) space complexity. No division method. Its prefix and postfix solution. although it is optimal in terms of time complexity, it uses extra space for prefix and postfix arrays.
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # There is a challenge to complete this problem without using division
        # So we will use prefix and postfix  which is two arrays for each of the operation where it calculates 
        # the product of all the values before that index
        # For example the input is [1,2,4,6] so 
        # prefix for this will be [1, 1, 2, 8]
        # Similary for postfix it is the same thing but from the opposite side
        # Postfix for the above example will be [48,24,6,1]
        # Now to get the output all we need is to multiply both arrays values at their respective indices
        # Output is [48,24,12,8]
        # Even though this solution is optimal in terms of time complexity, it uses too much space so lets try to tackle that

        result = [1] * len(nums)
        # Lets do prefix on the result array it self
        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix = prefix * nums[i]
        # Now lets calculate postfix and multiply to that index in the same array
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):

            result[i] = result[i] * postfix
            postfix = postfix * nums[i]

        return result
