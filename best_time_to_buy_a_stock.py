# Best Time to Buy and Sell Stock
# Solved 
# You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

# You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

# Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.

# Example 1:

# Input: prices = [10,1,5,6,7,1]

# Output: 6
# Explanation: Buy prices[1] and sell prices[4], profit = 7 - 1 = 6.

# Example 2:

# Input: prices = [10,8,7,5,2]

# Output: 0
# Explanation: No profitable transactions can be made, thus the max profit is 0.

# Constraints:

# 1 <= prices.length <= 100
# 0 <= prices[i] <= 100


# Solution

# First Approach: Brute Force. This is what I came up by my own. Time complexity is O(n^2) and space complexity is O(1)

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # First lets try to write a brute force solution by iterating through the array twice. The time complexity is
        # O(n) and memory is O(1)

        # The solution is to iterate through the array twice where I buy at every index and sell at every index after that and see the max profit


        res = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                res = max(res,prices[j] - prices[i])

        return res
    

# Second Approach: Two pointers with sliding window. Time complexity is O(n) and space complexity is O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Lets try the two pointer with sliding window approach. 
        # The idea is simple. We have two pointers. Initially, left pointer at 0 and right pointer at 1 and then see if
        #  if the right pointer is greater than the left pointer. 
            # If it is then calculate the profit and see if it is greater than the current profit and also increase the right pointer by 1 so that you calculate every max profit with that current min buy
            # If right is less than or equal to the left then move the left pointer to where right pointer is and move the right pointer by 1

        # Lets code up the solution

        l, r = 0, 1
        res = 0

        while r < len(prices):
            if prices[l] >= prices[r]:
                l = r
            else:
                res = max(prices[r] - prices[l], res)
            r += 1
        return res

        
# Third Approach: Dynamic Programming. Time complexity is O(n) and space complexity is O(n)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Lets look at another solution which uses dynamic programming. Here instead of tracking just the maxProfit
        # You also track the minBuy for every index
        # At every iteration you update both the values by checking if the current profit (current index - minBuy ) is greater or not and also by checking 
        # If the minBuy is actually cheapest buy or not by comparing it to the current index

        minBuy = prices[0]
        maxProfit = 0

        for i in prices:
            maxProfit = max(maxProfit, i - minBuy)
            minBuy = min(minBuy, i)

        return maxProfit


        
