class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k +=1
        return k

"""
2 pointer i and k if k is equal to value the increment i
if i is not equalt to value the update k with i

Time COmplexity: O(n)
"""