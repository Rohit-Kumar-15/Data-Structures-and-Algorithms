class Solution:
    def trimMean(self, arr: list[int]) -> float:
        arr.sort()
        r = int(len(arr)*0.05)
        sums = 0
        for i in range(r, len(arr)-r):
            sums += arr[i]
        avg = sums / (len(arr)-r*2)
        return avg

"""
first we find out how many elements are 5% of element
then run a loop in between 90% of elements and sum

Time Complexity: O(n)
Space Complexity: O(1)
"""