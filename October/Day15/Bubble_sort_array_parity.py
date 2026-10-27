class Solution:
    def sortArrayByParity(nums):
        l = 0
        for i in range(len(nums)):
            for j in range(len(nums)-i-1):
                if nums[j] % 2 > nums[j + 1] % 2:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return nums

    print(sortArrayByParity([7,12,3,8]))

"""
we run a nested for loop and check if an odd no comes before an even if it does we swap their place

Time Complexity: O(n^2)
Space Complexity: O(1)
"""