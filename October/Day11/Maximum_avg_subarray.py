
class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        s = float('-inf')

        for i in range(len(nums) - k + 1):
            sums = 0
            for j in range(i, i + k):
                sums += nums[j]

            avg = sums / k
            if avg > s:
                s = avg

        return s

"""
iterate through len-k+1
sum and average elements of subarray
if avg is greater than global avg then update

Time Complexity: O(n^2)
"""
class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        max_avg = float('-inf')
        j = 0
        sums = 0
        for i in range(len(nums)):
            sums += nums[i]

            if i-j+1 == k:
                max_avg = max(max_avg, sums/k)
                sums -= nums[j]
                j += 1
        return max_avg

"""
sliding window approach when loop is window size check average and update and remove the last element
next iter add element and average and check, update

Time Complexity: O(n)
"""
