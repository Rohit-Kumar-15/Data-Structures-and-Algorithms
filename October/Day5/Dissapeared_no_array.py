class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        S = set(nums)
        result = []

        for i in range(1, len(nums)+1):
            if i not in S:
                result.append(i)
        return result

"""
make a set of nums since it stores unique elements
iterate throught length and add nos not in set to result

Time Complexity : O(n)
"""