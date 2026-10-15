class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        S1 = set(nums1)
        S2 = set(nums2)
        result = []
        for i in S1:
            if i in S2:
                result.append(i)
        return result
    
"""
convert both element to sets so that they both have unique elements
iterate through on eand check if other has it if yes the append to array

Time Complexity: O(n)
"""