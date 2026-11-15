class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(1, n // 2 + 1):
            if n % i == 0 and s[:i] * (n // i) == s:
                return True
        
        return False

"""
we iterate through 1 to length/2 iterations and in every iteration we check if n is a valid divisor of i
and if multiplying the substring we get the original string or not

Time Complexity: O(n^2)
Space Complexity : O(1)
"""