def insertionSort(nums):
    for i in range(1, len(nums)):
        current = nums[i]
        j = i-1
        while j>=0 and nums[j] > current:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = current
    return nums

print(insertionSort([5,8,2,1,3,9]))

"""
we start for index 1 and check if any of the previous element is greater if it is we move it to next index 
once we encounter a smaller element we place the current element in the index we checked before

Time Complexity: O(n^2)
Space Complexity: O(1)
"""