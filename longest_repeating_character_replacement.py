# Longest Repeating Character Replacement
# Solved 
# You are given a string s consisting of only uppercase english characters and an integer k. You can choose up to k characters of the string and replace them with any other uppercase English character.

# After performing at most k replacements, return the length of the longest substring which contains only one distinct character.

# Example 1:

# Input: s = "XYYX", k = 2

# Output: 4
# Explanation: Either replace the 'X's with 'Y's, or replace the 'Y's with 'X's.

# Example 2:

# Input: s = "AAABABB", k = 1

# Output: 5
# Constraints:

# 1 <= s.length <= 1000
# 0 <= k <= s.length


# Approach 1: Sliding Window with HashMap

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Dictionary to keep track of character counts in the current window
        count = {}
        # Result variable to store the maximum length found
        res = 0

        # Left pointer for the sliding window
        l = 0
        # Tracks the count of the most frequent character in the window
        maxf = 0

        # Right pointer moves through the string
        for r in range(len(s)):
            # Increment the count for the current character
            count[s[r]] = 1 + count.get(s[r], 0)
            # Update maxf to the highest frequency in the window
            maxf = max(maxf, count[s[r]])

            # If the number of characters to change exceeds k, shrink window from left
            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1

            # Update res with the largest window size found so far
            res = max(res, r - l + 1)

        # Return the length of the longest valid substring
        return res