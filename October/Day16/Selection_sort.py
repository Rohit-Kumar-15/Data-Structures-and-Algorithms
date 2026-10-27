def selectionSort(nums):
    for i in range(len(nums)-1):
        small = i
        for j in range(i+1,len(nums)):
            if nums[small] > nums[j]:
                small = j
        nums[i] , nums[small] = nums[small], nums[i]
    return nums

print(selectionSort([5,2,8,3,1,10]))

"""
we use a nested loop to iterate through the array keeping track of the minimum element in each iteration
and the swap it with the indexes of the outer loop sorting them

Time Complexity: O(n^2)
Space Complexity: O(n)
"""

        