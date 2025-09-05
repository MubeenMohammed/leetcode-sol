# Longest Substring Without Repeating Characters
# Solved 
# Given a string s, find the length of the longest substring without duplicate characters.

# A substring is a contiguous sequence of characters within a string.

# Example 1:

# Input: s = "zxyzxyz"

# Output: 3
# Explanation: The string "xyz" is the longest without duplicate characters.

# Example 2:

# Input: s = "xxxx"

# Output: 1
# Constraints:

# 0 <= s.length <= 1000
# s may consist of printable ASCII characters.



# Approach 1: Brute Force

#  The solution is simple enough. You just iterate through the array twice and keep track of the current substring without duplicate characters
# If you find a duplicate character then break the inner loop and move to the next character in the outer loop
# Time complexity is O(n^2) and space complexity is O(1)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Lets first try the brute force way
        if len(s) == 0:
            return 0 
        temp = ''
        res = 1
        for i in range(len(s)):
            temp = s[i]
            for j in range(i+ 1, len(s)):
                print(temp)
                if s[j] not in temp:
                    temp += s[j]
                    res = max(res, len(temp))
                else:
                    break
        return res
    

# Approach 2: Sliding Window with HashSet
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Here the method used is sliding window where 
        # you capture the substring in the set and 
        # if the duplicate character shows up then you trim the string from the left

        
        if len(s) == 0: return 0
        charSet = set()
        res = 0
        count = 0
        for i in range(len(s)):
            while s[i] in charSet:
                charSet.remove(s[count])
                count += 1
            charSet.add(s[i])
            res = max(res, i - count + 1)
        return res