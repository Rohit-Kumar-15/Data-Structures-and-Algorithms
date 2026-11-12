import sys

class Solution:
    def kthLargest(self, a, k):
        arr = list(a)
        target = len(arr) - k          # index in ascending order
        lo, hi = 0, len(arr) - 1
        while True:
            if lo == hi:
                return arr[lo]
            pivot = arr[(lo + hi) // 2]
            i, j = lo, hi
            while i <= j:
                while arr[i] < pivot:
                    i += 1
                while arr[j] > pivot:
                    j -= 1
                if i <= j:
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1
                    j -= 1
            if target <= j:
                hi = j
            elif target >= i:
                lo = i
            else:
                return arr[target]

def main():
    data = sys.stdin.read().split()
    n, k = int(data[0]), int(data[1])
    salaries = list(map(int, data[2:2 + n]))
    print(Solution().kthLargest(salaries, k))

if __name__ == "__main__":
    main()

"""
Approach: Quickselect (partitioning around a pivot). Only the partition that contains the target index is searched further.
Time Complexity : O(n) average, O(n^2) worst case
Auxiliary Space : O(1) beyond the copy
"""
