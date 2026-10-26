def optimized_bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        swapped = False
        
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                
        if not swapped:
            break
            
    return arr

print(optimized_bubble_sort([8,4,2,10,1]))

"""
we run the bubble sort algo but keep track if the inner loop swaped any element or not if it did not
swap any element then the array is sorted

Time Complexity: O(n^2)
Space Complexity: O(1)
"""