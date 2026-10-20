class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        l = 0
        for i in range(len(nums)):
            if nums[i]%2 == 0:
                nums[l],nums[i] = nums[i],nums[l]
                l += 1
        return nums

"""
1 pointer at left when we encounter an even we swap with currnet no

Time Complexity: O(n)
"""