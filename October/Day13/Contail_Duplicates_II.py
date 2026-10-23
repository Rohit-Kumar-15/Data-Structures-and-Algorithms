class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j] and abs(i-j) <= k:
                    return True
        return False

"""
run a nested loop and check if elements of indices i and j are same such that i-j should be less than equal to k

Time Complexity: O(n^2)
"""