class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        l = 0
        r = len(nums)-1
        res = [0]*len(nums)
        for i in range (len(nums)-1, -1, -1):
            if abs(nums[l]) > abs(nums[r]):
                res[i] = nums[l]**2
                l += 1
            else:
                res[i] = nums[r]**2
                r -= 1
        return res

"""
since largest squares will be at the extreme of the array
we use two pointers l and r and the wone greatest will be put at the end of the result array

Time Complexity: O(n)
"""