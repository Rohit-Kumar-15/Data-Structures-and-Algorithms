class Solution:
   def reverseVowels(self, s: str) -> str:
       v = set("aeiouAEIOU")
       s = list(s)
       l = 0
       r = len(s)-1
       while l < r:
           if s[l] not in v:
               l += 1
           elif s[r] not in v:
               r -= 1
           else:
               s[l], s[r] = s[r], s[l]
               l += 1
               r -= 1
       return "".join(s)

"""
use 2 pointers from both side if we run into vowels we switch them

Time Complexity : O(n)
"""