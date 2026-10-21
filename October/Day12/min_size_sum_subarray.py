class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        l = 0
        sums = 0
        min_len = float('+inf')
        for r in range(len(nums)):
            sums += nums[r]

            while sums >= target:
                min_len = min(min_len, r-l+1)
                sums -= nums[l]
                l += 1
        if min_len == float('+inf'):
            return 0
        return min_len

"""
we use dynamic sliding window approach run r pointer to iterate throughout the array
the left pointer checks the condition if sums >= target then it stores the minimum length
and subtract the current element and move the left pointer

Time Complexity: O(n)
Space Complexity: O(1)
"""