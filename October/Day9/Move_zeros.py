class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
         l = 0
         for r in range(len(nums)):
            if nums[r] != 0:
                nums[l],nums[r] = nums[r],nums[l]
                l += 1

"""
run 2 pointers ole keep track of z other checks if no i not zero then it swaps with zero pointer

Time Complexity: O(n)
"""