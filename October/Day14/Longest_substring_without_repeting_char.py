class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = [0]*26
        left = 0
        max_len = 0

        for right in range(len(s)):
            freq[ord(s[right])-ord('a')] += 1

            while freq[ord(s[right])-ord('a')] > 1:
                freq[ord(s[left])-ord('a')] -= 1
                left += 1
            max_len = max(max_len, right-left+1)
        
        return max_len
"""
works only for small case letters
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = {}
        left = 0
        max_len = 0

        for right in range(len(s)):
            ch = s[right]
            freq[ch] = freq.get(ch, 0) + 1

            while freq[ch] > 1:
                freq[s[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len

"""
run a sliding window keeping track of frequency of each element in the sliding window
if frequency exceeds 1 then shrink the window until condition is satisfied return max len of window

Time Complexity: O(n)
Space Complexity: O(n)
"""