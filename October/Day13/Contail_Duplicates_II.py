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

class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        seen = {}

        for i, val in enumerate(nums):
            if val in seen and i - seen[val] <= k:
                return True
            else:
                seen[val] = i
        
        return False

"""
we can use a hashmap, save the element as key and the index as value when we encounter the same no we check if it is within
k distance i.e i - value(for element) <= k then return true else false

Time Complexity: O(n)
"""