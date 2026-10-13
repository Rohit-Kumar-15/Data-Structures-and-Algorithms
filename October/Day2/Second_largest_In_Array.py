class solution:
    def getSecondLargest(arr):
        n = len(arr)
        max = -1
        secondLargest = -1

        for i in range(n):
            if arr[i] > largest:
                largest = arr[i]

        for i in range(n):
            if arr[i] > secondLargest and arr[i] != largest:
                secondLargest = arr[i]
        
        return secondLargest

"""
first we find the largest with one traversal
then we find the second largest with the second largest

Time Complexity: O(n)
"""