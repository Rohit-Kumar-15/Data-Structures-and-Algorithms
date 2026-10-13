class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        result = [nums[0]]

        for i in range(1, len(nums)):
            result.append(result[i-1] + nums[i])

        return result

"""
we set the first element as the same
for the next result element we just add the next element form the nums and previous element form the result

Time Complexity : O(n)
"""