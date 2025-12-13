# 560. Subarray Sum Equals K
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

 

# Example 1:

# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:

# Input: nums = [1,2,3], k = 3
# Output: 2
 

# Constraints:

# 1 <= nums.length <= 2 * 104
# -1000 <= nums[i] <= 1000
# -107 <= k <= 107


class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # We can use a prefix sum to track the previous sums and check if cur_sum - target is available in the prefix sum and if yes how many times and you add that value to the result
        # Example:
        # [1, 1, 1], k = 2
        # You can intialize the map to {0: 1} since you have prefix sum of 0 which is taking none of the values
        # Now iterate through the array one by one
        # sum([1]) = 1
        # 1 - 2 (target) = 1. Is there a 1 in the prefix sum hashmap which we can remove from our sub array to get our target? No since the only value we have in the 0:1 in our prefix hashmap
        # since now we have a sum of 1. we can add that to our count so new_hashmap = {0:1, 1:1}
        # Lets move on to the next value which 1 again
        # Sum is 1 + 1 = 2
        # Sum - Target = 2 -2 = 0
        # Do we have 0 in the prefix map? Yes and how many times - 1
        # So now we can add 1 to the res and also add sum 2 in the prefix sum map - {0:1,1:1, 2:1}
        
        #Let move on to the next value which is 1 again
        # Sum is 1 + 1 + 1 = 3
        # Sum - target = 3 - 2 = 1
        # Do we have 1 in the prefix map? Ues and how many times - 1
        # So now we add 1 to the res and also add sum 3 in the prefix sum map  {0:1,1:1,2:1, 3:1}
        # The end as we reached the final position of the array 
        # Final result is 2
        
        # Now lets code this solution

        res = 0
        prefix_sum = {}
        prefix_sum[0] = 1
        cur_sum = 0
        for n in nums:
            cur_sum += n
            if (cur_sum - k) in prefix_sum:
                res += prefix_sum[cur_sum - k]
            prefix_sum[cur_sum] = 1 + prefix_sum.get(cur_sum, 0)
        return res

