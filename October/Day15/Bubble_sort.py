class Solution:
    def bubbleSort(self,arr):
        for i in range(len(arr)):
            for j in range(len(arr)-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        
        return arr

"""
compare adjacent elements if the current element is greater than the previous one then switch
run a nested loop to iterate through all elements

Time Complexity: O(n^2)
Space Complexity: O(1)
"""
