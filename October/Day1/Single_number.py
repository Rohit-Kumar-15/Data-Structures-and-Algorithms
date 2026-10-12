class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        xor = 0
        for i in nums:
            xor = xor ^ i
        return xor

""" 
a xor a = 0, pairs cancel each other
a xor 0 = a, Keep value

we add each number if its a pair then it cancels each other

Time Complexity : O(n)
Space complexity : O(1)
"""