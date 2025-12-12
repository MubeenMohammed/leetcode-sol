# 55. Jump Game
# Attempted
# Medium
# Topics
# premium lock icon
# Companies
# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.

 

# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:

# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 

# Constraints:

# 1 <= nums.length <= 104
# 0 <= nums[i] <= 10


# Solution

# Brute force method using trying all the possible jumps from 0, nums[i] and backtracking if failed
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # A brute force method would be try all the possible jumps and see if you reach last index or not
        # Lets try to code the brute force approach
        if len(nums) == 1:
            return True
        elif nums[0] == 0:
            return False
        for i in range(1, nums[0] + 1):
            if self.canJump(nums[i:len(nums)]):
                return True
            else:
                continue
        return False
            

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #A optimal solution
        # First intialize variable goal which is first set to the last index of nums array since that is our original goal
        # Then start loop from the last second index and see if we reach our goal(i.e., last index) assuming we reach at the current index 

        # Eg: [2,3,1,1,4]
        # goal = 4
        # cur_index = 3 and max_jump = 1
        # 3 + 1 >= 4 (This is true)
        # Update the goal to index 3 since we can reach index 4 from 3 

        # Condition is curr_index + max_jump_of_cur_index >= goal if yes update the goal, if not then continue traversing the array in the same order

        # At the end check if the goal became 0 or not if it is not zero then we know for sure the goal cannot be reached 

        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        return True if goal == 0 else False

        

        