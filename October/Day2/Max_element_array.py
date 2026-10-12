class Solution:
    def largest(self, arr: list[int]) -> int:
        largest_num = arr[0]

        for i in range(1, len(arr)):
            if arr[i] > largest_num:
                largest_num = arr[i]

        return largest_num

"""
assign first as max iterate and comare for nos greater if found assign to max

Time Complexity: O(n)
"""