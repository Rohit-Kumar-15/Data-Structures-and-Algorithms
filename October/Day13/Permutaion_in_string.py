class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = [0] * 26
        s2_count = [0] * 26

        for i in s1:
            s1_count[ord(i) - ord('a')] += 1
        
        for i in range(len(s2)):
            s2_count[ord(s2[i]) - 97] += 1

            if i >= len(s1):
                s2_count[ord(s2[i - len(s1)]) - 97] -= 1
            
            if s1_count == s2_count:
                return True
        
        return False

"""
we make the frequency array if elements in s1
then we compare the frequencies with the sliding window if freq matches return True.

Time Complexity: O(n)
Space Complexity: O(1)
"""