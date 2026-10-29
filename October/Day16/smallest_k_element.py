def smallestKElemenys( nums, k):
    smallest = []
    for i in range(len(nums)):
        small = i
        for j in range(i+1, len(nums)):
            if nums[small] > nums[j]:
                small = j
        nums[i], nums[small] = nums[small], nums[i]

    for i in range(k):
        smallest.append(nums[i])
    return smallest

print(smallestKElemenys([6,12,0,9,3,17], 3))

"""
Sort the element and append k elements to an array and return

Time compexity: O(n^2)
Space Complexity: O(n)
"""