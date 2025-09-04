# Trapping Rain Water
# Solved 
# You are given an array of non-negative integers height which represent an elevation map. Each value height[i] represents the height of a bar, which has a width of 1.

# Return the maximum area of water that can be trapped between the bars.

# Example 1:



# Input: height = [0,2,0,3,1,0,1,3,2,1]

# Output: 9
# Constraints:

# 1 <= height.length <= 1000
# 0 <= height[i] <= 1000

#  Prefix & Suffix Arrays

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        # Basically You can solve this problem in two ways one using O(n) time and O(n) memory 
        # Another way to solve this problem is using same time complexity but O(1) memory using two pointer
        # Lets look at the first solution

        # Go through the array and calculate the current index right max height and left max height
        # Then calculate the min of those two max 
        # To get the current index capacity, you can just do min(leftMax, rightMax) - curIndex

        leftMax = []
        currentLeftMax = 0
        for i in height:
            currentLeftMax = max(i, currentLeftMax)
            leftMax.append(currentLeftMax)
        
        rightMax = [0] * len(height)
        currentRightMax = 0
        for i in range(len(height) - 1, -1, -1):
            currentRightMax = max(height[i], currentRightMax)
            rightMax[i] = currentRightMax

        
        res = 0
        for i in range(len(height)):
            area = min(leftMax[i], rightMax[i]) - height[i]
            if (area > 0):
                res += area
        return res
    


# Two Pointer Approach

class Solution:
    def trap(self, height: List[int]) -> int:
        # Basically You can solve this problem in two ways one using O(n) time and O(n) memory 
        # Another way to solve this problem is using same time complexity but O(1) memory using two pointer
        # Lets look at the first solution

        # Go through the array and calculate the current index right max height and left max height
        # Then calculate the min of those two max 
        # To get the current index capacity, you can just do min(leftMax, rightMax) - curIndex

        # Now lets try two pointer solution to avoid excess use of memory

        if not height:
            return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res
