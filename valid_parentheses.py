# Valid Parentheses
# Solved 
# You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

# The input string s is valid if and only if:

# Every open bracket is closed by the same type of close bracket.
# Open brackets are closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
# Return true if s is a valid string, and false otherwise.

# Example 1:

# Input: s = "[]"

# Output: true
# Example 2:

# Input: s = "([{}])"

# Output: true
# Example 3:

# Input: s = "[(])"

# Output: false
# Explanation: The brackets are not closed in the correct order.

# Constraints:

# 1 <= s.length <= 1000

class Solution:
    def isValid(self, s: str) -> bool:
        # Lets use stack and solve this 
        # Go through each character in the string and check if it is left parentheses or right
        # If its left then add to the stack
        # If its right then pop the stack and compare if it is valid ( if it is other half of the current right) then continue
        # If it is not valid then return false 

        # First lets make a dictionary for each right bracket

        # Tracker to pair the valid parentheses
        tracker = {
            "}": "{",
            ")": "(",
            "]": "["
        }

        # Intialize the stack
        stack = []
        counter = 0
        # Loop through the characters in the given string
        for c in s:
            # If the character is the one of the left parentheses then add/append it to the stack
            if c not in tracker:
                print("First condition",c)
                stack.append(c)
            # If the character is one of the right parentheses then pop and check if has valid right left parentheses or not
            if c in tracker:
                if stack and stack[-1] == tracker[c]:
                    stack.pop()
                else:
                    return False

        return False if stack else True