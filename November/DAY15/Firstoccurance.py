class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        h = len(haystack)

        for i in range(0, h-n+1):
            j = 0

            while j < n and haystack[i+j] == needle[j]:
                j += 1

            if j == n:
                return i
        return -1

"""
use the sliding window approach when we encounter the char equal to first char in needle we check if the subsequient 
characters are equal as well

Time Complexity: O(n)
Space Complexity: O(1)
"""