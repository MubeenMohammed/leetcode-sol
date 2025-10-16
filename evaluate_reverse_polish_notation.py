# Evaluate Reverse Polish Notation
# Solved 
# You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.

# Return the integer that represents the evaluation of the expression.

# The operands may be integers or the results of other operations.
# The operators include '+', '-', '*', and '/'.
# Assume that division between integers always truncates toward zero.
# Example 1:

# Input: tokens = ["1","2","+","3","*","4","-"]

# Output: 5

# Explanation: ((1 + 2) * 3) - 4 = 5
# Constraints:

# 1 <= tokens.length <= 1000.
# tokens[i] is "+", "-", "*", or "/", or a string representing an integer in the range [-100, 100].

from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        # This is simple and easy. Every time you hit one of the operands, you pop the last two stack elements
        # Perform the operation and add the result back to the stack so that we can continue the operations
        # If is not one of the operands then simply add it to the stack to be popped later on in the loop
        
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a))
            else:
                stack.append(int(c))
        return stack[0]