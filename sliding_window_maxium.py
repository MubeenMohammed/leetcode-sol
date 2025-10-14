# Sliding Window Maximum
# Solved 
# You are given an array of integers nums and an integer k. There is a sliding window of size k that starts at the left edge of the array. The window slides one position to the right until it reaches the right edge of the array.

# Return a list that contains the maximum element in the window at each step.

# Example 1:

# Input: nums = [1,2,1,0,4,2,6], k = 3

# Output: [2,2,4,4,6]

# Explanation: 
# Window position            Max
# ---------------           -----
# [1  2  1] 0  4  2  6        2
#  1 [2  1  0] 4  2  6        2
#  1  2 [1  0  4] 2  6        4
#  1  2  1 [0  4  2] 6        4
#  1  2  1  0 [4  2  6]       6
# Constraints:

# 1 <= nums.length <= 1000
# -10,000 <= nums[i] <= 10,000
# 1 <= k <= nums.length


# The first way that I tried is the brute force way where I will traverse the array and for each window I will find the max element and append it to the result array
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Lets try writing a brute force solution
        # Loop through the array twice and find the maxium element in the window. This might O(n * k) since there is a nested for loop
        if len(nums) == 0: return []
        l = 0
        r = k
        res = []
        while (r - 1) != len(nums):
            cur_max = -10000
            for i in range(l, r):
                cur_max = max(nums[i], cur_max)
            l += 1
            r += 1
            res.append(cur_max)
        return res
    
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Now lets try to optimize the solution 
        #  Lets solve this using the deque method which takes O(n)

        # We have left and right pointers set to 0 i.e, 
        l = r = 0
        # Our normal deque. Here we track indices instead of normal array values since we can easily get the value and also it some things easier
        q = deque() 
        # Finally our result which is to return at the end
        res = []

        while r < len(nums):
            # Before adding the element to the deque, we need to check if this is the highest element or not
            # You check if the deque is empty or not. If it is not empty then check if the right most element is smaller than element we are trying to add
            # If it is smaller then pop that element from the deque
            while q and nums[q[-1]] < nums[r]:
                q.pop() 

            # Finally add that element in deque
            q.append(r)

            # Now check if we have to remove the leftmost element in the deque since the window has decreased from the left
            if l > q[0]:
                q.popleft()
            
            # Now to update the result and the pointers, we increase the r value by one each iteration
            # Now to add to the output array the leftmost(biggest element) in the window, 
            # we need to check if the window size has been reached or not which we can do by
            # Intially we do not reach the window since l and r start at the same point, but after certain point r+1 becomes greater than k which means every new iteration is a new window
            if (r + 1) >= k:
                res.append(nums[q[0]])
                l += 1
            r += 1

        # Now all there is to return the result
        return res



    






