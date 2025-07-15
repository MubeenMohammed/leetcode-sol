import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Now to figure out how to clean the string to get the new_s
        new_s = re.sub('[^A-Za-z0-9]+', '', s).lower()
        # Assuming I have a combined string new_s
        # If the length is not even then automatically its not a palindrome
        if len(new_s) == 1:
            return True
        front_pointer = 0
        back_pointer = len(new_s) - 1
        for i in range(len(new_s) // 2):
            if new_s[front_pointer] != new_s[back_pointer]:
                return False
            front_pointer += 1
            back_pointer -= 1
        return True
        