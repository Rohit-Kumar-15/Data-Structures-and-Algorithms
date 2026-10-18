class Solution:
    def reverseString(self, s: str) -> str:
        # code here
        rs = ""
        l = len(s)-1
        while l>= 0:
            rs += s[l]
            l -= 1
            
        return rs

"""
we run a reverse while loop and append the characters

Time Complexity : O(n)
"""