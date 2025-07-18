# Container With Most Water
# Solved 
# You are given an integer array heights where heights[i] represents the height of the 
# i
# t
# h
# i 
# th
#   bar.



# You may choose any two bars to form a container. Return the maximum amount of water a container can store.

# Example 1:



# Input: height = [1,7,2,5,4,7,3,6]

# Output: 36
# Example 2:

# Input: height = [2,2,2]

# Output: 4
# Constraints:

# 2 <= height.length <= 1000
# 0 <= height[i] <= 1000


# Solution:

# Ofocurse like always there is a brute force method where you can check every combination of two bars and find the maximum area

from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Okay lets solve this problem in brute force which I think should be simple enough
        result = 0
        for i in range(len(heights)):
            for j in range(i, len(heights)):
                # Calculate the area of the rectangle
                # Get the minimum of two heights and that will be the height of the container
                ch = min(heights[i], heights[j])
                cw = j - i
                area = ch * cw
                result = max(result,area)

        return result
    

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Lets try a fluke using two pointer solution. 
        # Now what I am thinking is there are two pointers one at the front of the list and one at the back
        # You calculate the area and save it in a variable.
        # Now you compare both heights and check which height is less
        # If front pointer height is less then move it to one right and 
        # Similary if the back pointer height is less then move it to one left and calculate the area and keep the max area

        # Lets code this fluke solution

        fp = 0
        bp = len(heights) - 1
        result = 0

        while fp < bp:
            area = min(heights[fp], heights[bp]) * (bp - fp)
            result = max(result, area)
            if heights[fp] < heights[bp]:
                fp += 1
            else:
                bp -= 1
        return result

    # The fluke worked. :) Fun Fact from Kevin from the office: Fluke is one of the most common fish in the ocean. ;)