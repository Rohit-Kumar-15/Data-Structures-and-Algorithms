from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1

        for j in range(1, len(nums)):
            if nums[j] != nums[i - 1]:
                nums[i] = nums[j]
                i += 1
        
        return i

"""
initialize i and j as 1 since first element is always unique
iterate j if i-1 is not equal to j then update i and increment both

return i the no of unique element

Time Complexity : O(n)
"""