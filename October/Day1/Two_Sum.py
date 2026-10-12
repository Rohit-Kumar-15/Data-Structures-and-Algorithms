class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                sum = nums[i] + nums[j]
                if sum == target:
                    return [i, j]

"""Basic brute force approach run a nested loops to find each pair and check if the sum is equal to target
we deliberately run the inner loop an index ahead so it won't add the same element twice
Time complexity : O(n^2)"""