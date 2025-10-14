# Minimum Window Substring
# Solved 
# Given two strings s and t, return the shortest substring of s such that every character in t, including duplicates, is present in the substring. If such a substring does not exist, return an empty string "".

# You may assume that the correct output is always unique.

# Example 1:

# Input: s = "OUZODYXAZV", t = "XYZ"

# Output: "YXAZ"
# Explanation: "YXAZ" is the shortest substring that includes "X", "Y", and "Z" from string t.

# Example 2:

# Input: s = "xyz", t = "xyz"

# Output: "xyz"
# Example 3:

# Input: s = "x", t = "xy"

# Output: ""
# Constraints:

# 1 <= s.length <= 1000
# 1 <= t.length <= 1000
# s and t consist of uppercase and lowercase English letters.



class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #First check if the t string is empty. if it is then return ""
        if t == "":  return ""
        #Initialize two hashmaps to track the counts of both strings
        t_count, window = {}, {}

        # Now populate the first hashmap by counting the no of characters in t
        for char in t:
            # Python has a get function in the hashmap where we can pass a default value when that key doesnt exists
            t_count[char] = 1 + t_count.get(char, 0)

        #Now initialize the res, resLen, l and r pointer
        res, resLen = [-1, -1], float("infinity")
        
        # Intialize the left pointer to be 0
        l = 0
        
        #We also need have and need values to check if these two values are equal or not
        #need is the no of unique characters in t string
        #have is the count we track to check if how many characters in our window has same count as in the t string
        #e.g: Input: s = "OUZODYXAZV", t = "XYZ". If our window is OUZ then the need is always constant which is 3 but the have is 1 since we only have Z character same count as in our t-string
        have, need = 0, len(t_count)
        #Our right pointer is a counter in the for loop
        for r in range(len(s)):
            #First you add the s[r] in our window i.e same as above but with char in s instead of t
            window[s[r]] = 1 + window.get(s[r], 0)
            
            #Now check if s[r] is in the t_count and if our window has same count as our t_count[s[r]]
            if s[r] in t_count and window[s[r]] == t_count[s[r]]:
                #If the condition is successful then increase the have count
                have += 1

            #Now check if the have == need
            while have == need:
                #First we need to check if the length of the current window is smaller than what we already had
                if (r-l+1) < resLen:
                    #Update the len and also update the res window too
                    resLen = r-l+1
                    res = [l, r]
                
                #Now remove the leftmost character in the window and check other windows
                window[s[l]] = window[s[l]] - 1

                #Check if this decreases our have count or not
                if s[l] in t_count and window[s[l]] < t_count[s[l]]:
                    have -= 1

                #Move the left pointer to the right by 1 
                l += 1
        l, r = res

        return s[l:r+1] if resLen != float("infinity") else ""

        #Time Complexity: O(n+m): n= length of the s string m is the total unique characters in t and s
        #Space complexity O(m): m = the total unique characters in t and s


        