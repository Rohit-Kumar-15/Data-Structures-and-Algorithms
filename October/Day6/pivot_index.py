class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total = sum(nums)
        leftsum = 0

        for i in range(len(nums)):
            rightsum = total - leftsum -nums[i]
            if leftsum == rightsum:
                return i
            
            leftsum += nums[i]
        return -1

"""
sum of right  = sum of left
sum of rigth = total - sum of left - current no

Time Complexity: O(n)
"""