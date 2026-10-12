class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if(nums[i] == nums[j]):
                    return True
        return False

"""Basic brute force approach run a nested loops to find each pair and check if it is same as the element
we deliberately run the inner loop an index ahead so it won't compare the same element and return incorrect answer
Time complexity : O(n^2)"""