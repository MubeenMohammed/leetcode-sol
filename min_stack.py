# Minimum Stack
# Solved 
# Design a stack class that supports the push, pop, top, and getMin operations.

# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# Each function should run in 
# O
# (
# 1
# )
# O(1) time.

# Example 1:

# Input: ["MinStack", "push", 1, "push", 2, "push", 0, "getMin", "pop", "top", "getMin"]

# Output: [null,null,null,null,0,null,2,1]

# Explanation:
# MinStack minStack = new MinStack();
# minStack.push(1);
# minStack.push(2);
# minStack.push(0);
# minStack.getMin(); // return 0
# minStack.pop();
# minStack.top();    // return 2
# minStack.getMin(); // return 1
# Constraints:

# -2^31 <= val <= 2^31 - 1.
# pop, top and getMin will always be called on non-empty stacks.


class MinStack:

    def __init__(self):
        self.stack = []
        # To implement the getMin() in constant time we use two stacks. One stack to store the data and 
        # Another stack to track the minimum value at each point
        self.minStack = []


    def push(self, val: int) -> None:
        # First you push the value to our normal stack to track the data
        self.stack.append(val)
        # Now you calculate if the new value is smaller than the previous minimum by looking into the top value of minStack
        # prevMin = self.minStack[-1]
        # There is also an edge case where the minStack is empty and we are trying to pop the top element which does exists. To avoid this problem, we do
        prevMin = self.minStack[-1] if self.minStack else val
        # Compare and check if the new value is the new min at that point
        newMin = min(prevMin, val)
        self.minStack.append(newMin)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        
