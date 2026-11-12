import sys

class Solution:
    def merge(self, intervals):
        intervals = self.mergeSort(intervals)
        result = []
        for s, e in intervals:
            if result and s <= result[-1][1]:
                if e > result[-1][1]:
                    result[-1][1] = e
            else:
                result.append([s, e])
        return result

    def mergeSort(self, a):
        if len(a) <= 1:
            return a
        mid = len(a) // 2
        left = self.mergeSort(a[:mid])
        right = self.mergeSort(a[mid:])
        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i][0] <= right[j][0]:
                merged.append(left[i]); i += 1
            else:
                merged.append(right[j]); j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    intervals = []
    for i in range(n):
        intervals.append([int(data[1 + 2 * i]), int(data[2 + 2 * i])])
    for s, e in Solution().merge(intervals):
        print(s, e)

if __name__ == "__main__":
    main()

"""
Approach: Sort intervals by start with merge sort, then sweep: an interval touching or overlapping the last merged one extends it, otherwise it starts a new block.
Time Complexity : O(n log n)
Auxiliary Space : O(n)
"""
