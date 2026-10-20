class Solution:
    def maxSubarraySum(self, arr, k):
        # code here 
        i = 0
        sums = 0
        total = float('-inf')
        for j in range(len(arr)):
            sums += arr[j]
            if j-i+1 == k:
                total = max(total, sums)
                sums -= arr[i]
                i += 1
        return total

"""
sliding window approach add and remove next and previous and next element and update max total when greater

Time Complexity : O(n)
Space complexity : O(1)
"""