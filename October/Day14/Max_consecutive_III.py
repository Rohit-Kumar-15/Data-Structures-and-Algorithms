class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        i = 0
        zeros = 0
        max_len = 0

        for j in range(len(nums)):
            if nums[j] == 0:
                zeros += 1

            while zeros > k:
                if nums[i] == 0:
                    zeros -= 1
                i += 1

            max_len = max(max_len, j - i + 1)

        return max_len

"""
we run a sliding window and check if no if zeros should be smaller than k if it is greater we shrink the window
until it satisfies the condition. we keep track of the largest consecutive window where the no of consecutive 
zerosis less than k

Time Complexity: O(n)

Space Complexity: O(1)
"""