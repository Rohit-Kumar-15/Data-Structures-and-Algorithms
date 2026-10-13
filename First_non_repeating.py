class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        element = {}

        for i in nums:
            if i not in element:
                element[i] = 1
            else:
                element[i] += 1

        for k,v in element.items():
            print("Element :", k,"\t", "Frequency :", v)

"""
define a dictionary
add distinct array elements
count their frequency and print

Time Complexity : O(n)
"""