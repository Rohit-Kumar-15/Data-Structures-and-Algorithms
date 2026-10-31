class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        midx = m - 1
        nidx = n - 1 
        right = m + n - 1

        while nidx >= 0:
            if midx >= 0 and nums1[midx] > nums2[nidx]:
                nums1[right] = nums1[midx]
                midx -= 1
            else:
                nums1[right] = nums2[nidx]
                nidx -= 1

            right -= 1

"""
we have 3 pointers m which keeps track of elemeents in nums1 n keeps track of elements in nums 2 and 
right keeps track of element in nums1 array from the end. we chwck which element is greater and place it
in n and decrement right

Time Complexity: O(n+m)
"""