class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        element = {}

        for i in nums:
            if i not in element:
                element[i] = 1
            else:
                element[i] += 1

        n = len(nums) // 2

        for key, value in element.items():
            if value > n:
                return key

        return 0

"""
define a dictionary
add distinct array elements
count their frequency 
if frequenci is more than n/2 the its mejority 

Time Complexity : O(n)
"""