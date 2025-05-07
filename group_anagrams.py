# Group Anagrams
# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Example 1:

# Input: strs = ["act","pots","tops","cat","stop","hat"]

# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
# Example 2:

# Input: strs = ["x"]

# Output: [["x"]]
# Example 3:

# Input: strs = [""]

# Output: [[""]]
# Constraints:

# 1 <= strs.length <= 1000.
# 0 <= strs[i].length <= 100
# strs[i] is made up of lowercase English letters.


#Solution
# The trick here is to count the frequency of character in each word and use that as key and values as the string that have same frequency list
# So if you have a list like say ["act","pots","tops","cat","stop","hat"]
# Then loop through the array and create frequency array of each string. What I mean by that is
# For lets says act, the frequency array is a: 1, c: 1, t: 1 and use this as key for dict and act as value of the key in the dict
# When I go the next string in the loop, you see if that similar frequency is already present in the dict and if it is then just append the string to the value array

# COMPLEXITY
# O(m * n) where m is the length of the list and n is the average length of the string

from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        memo_dict = defaultdict(list)
        for s in strs:
            frequency_dict = [0] * 26
            for char in s:
                frequency_dict[ord(char) - ord("a")] += 1
            memo_dict[tuple(frequency_dict)].append(s)
        return memo_dict.values()
