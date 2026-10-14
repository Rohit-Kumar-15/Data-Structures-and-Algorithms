class Solution:
    def missingNumber(self, nums):
        # Intuition: expected sum minus actual sum leaves the missing one
        n = len(nums)
        r = n * (n + 1) // 2
        for c in nums:
            r -= c
        return r

"""
sum of all nos till length of array - sum of numbers present = missing no

Time Complexity : O(n)
"""