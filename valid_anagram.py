# Valid Anagram
# Solved 
# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Example 1:

# Input: s = "racecar", t = "carrace"

# Output: true
# Example 2:

# Input: s = "jar", t = "jam"

# Output: false
# Constraints:

# s and t consist of lowercase English letters.

#SOLUTION
# First check if the lengths of both the strings are equal or not
    # If its not then return False or else continue to step 2
# Then collect the frequency of each character in the string1 in the dict
# Do the same for the second string as well
# Compare them and if it matches then its anagram orelse its not

# COMPLEXITY
# O(n)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_mem = {}
        t_mem = {}
        for char in s:
            if char in s_mem:
                s_mem[char] += 1
            else:
                s_mem[char] = 1
        for char in t:
            if char in t_mem:
                t_mem[char] += 1
            else:
                t_mem[char] = 1
        print(s_mem, t_mem)
        for char in s_mem:
            if char not in t_mem:
                return False
            if s_mem[char] != t_mem[char]:
                return False
        return True