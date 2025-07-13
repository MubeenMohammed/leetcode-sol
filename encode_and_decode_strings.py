# Encode and Decode Strings
# Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

# Please implement encode and decode

# Example 1:

# Input: ["neet","code","love","you"]

# Output:["neet","code","love","you"]
# Example 2:

# Input: ["we","say",":","yes"]

# Output: ["we","say",":","yes"]
# Constraints:

# 0 <= strs.length < 100
# 0 <= strs[i].length < 200
# strs[i] contains only UTF-8 characters.




# Solution:

# Basically we need to combine(encode) the list of strings into a single string and then decode it back to the original list of strings.
# Two functions for each operation

# We need a delimiter which will help us distinguish between different strings when decoding and we can use that delimiter to combine the strings while encoding.
# Since the strings can be made of any UTF-8 characters, we need a choose the delimiter in a way that it won't conflict with my strings.
# we can count length of strings and use that and a special character combined as a delimiter. 
# For each for ["neet","code","love","you"], we can use the delimiter as "4#neet4#code4#loves3#you" where 4 is the length of "neet", "code", "love" and 3 is the length of "you".

from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        # Adding the "length + #" as a delimiter before each string. Eg 4#neet4#code4#loves3#you
        result = ""
        for s in strs:
            length = len(s)
            result = result + str(length) + "#" + s
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            start = i
            slen = ''
            # Finding the length of the string until we hit the delimiter '#'
            while start < len(s) and s[start] != '#':
                slen = slen + s[start]
                start = start + 1
            start += 1
            # Now we have the length of the string, we can extract the string from the original string
            end = start + int(slen)
            result.append(s[start: end])
            i = end
        return result

