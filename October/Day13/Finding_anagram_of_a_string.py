class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        s_len = len(s)
        p_len = len(p)

        if s_len < p_len:
            return []
        
        p_count = [0] * 26
        s_count = [0] * 26
        res = []

        for i in p:
            p_count[ord(i) - ord('a')] += 1
        
        
        for i in range(s_len):
            s_count[ord(s[i]) - 97] += 1

            if i >= p_len:
                s_count[ord(s[i-p_len]) - 97] -= 1

            if p_count == s_count:
                res.append(i - p_len + 1)
        return res

"""
first we check if s is greter then p
we make the frequency array if elements in p
then we compare the frequencies with the sliding window if freq matches the we store the first index in res array

Time Complexity: O(n)
Space Complexity: O(1)
"""