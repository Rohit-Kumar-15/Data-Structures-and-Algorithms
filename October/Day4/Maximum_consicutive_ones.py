class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        left = 0
        res = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                left = right+1
            else:
                res = max(res, right-left+1)
        return res

    def findMaxConsecutiveOnesTwo(self, nums: list[int]) -> int:
        count = 0
        m = 0
        for i in nums:
            if i == 1:
                count +=1
            else:
                if m < count:
                    m = count
                count = 0
        if m < count:
            m = count
        return m

"""
either use sliding window and move the left pointer to the next index when ever encountering 0 

Or else we can count the no of ones if we encounter a 0  save the count and then reset it to 0 
and compare the counts and take the maximum

Time Complexity : O(n)
"""