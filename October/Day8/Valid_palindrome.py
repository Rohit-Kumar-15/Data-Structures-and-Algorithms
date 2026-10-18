class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            elif s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False
        return True

"""
we will iterate through the string form both side if we encounter a string will check if its alpha numeric
if not will move the pointer ahead. if we encounter an alha numeric string will check if bother the strings
are same in lower case, if not then False. if the string is finally palindrime then we return True.

Time Complexity : O(n)
"""