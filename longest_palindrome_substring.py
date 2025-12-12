# 5. Longest Palindromic Substring
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given a string s, return the longest palindromic substring in s.

 

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"
 

# Constraints:

# 1 <= s.length <= 1000
# s consist of only digits and English letters.


# So the brute force approach is to check every substring and see if its a palindrome
# But that would be O(n^3) time complexity


# A optimal solution would be start considering each character as a center and expand outwards by checking if the characters at both 
# ends are the same and if its then we continue expanding until they are not the same anymore. That is our palindrome.
# We do this for every character in the string and keep track of the longest palindrome we have seen so far.

class Solution(object):

    def longestPalindrome(self, s):
        # Lets try to do this without using dp table
        res = ''
        resLen = 0
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if resLen < (r - l + 1):
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if resLen < (r - l + 1):
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1
        return res
        
