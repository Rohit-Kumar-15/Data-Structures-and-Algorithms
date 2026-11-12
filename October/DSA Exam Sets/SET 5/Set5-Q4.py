import sys

class Solution:
    def countInversions(self, a):
        return self._sort(list(a))[1]

    def _sort(self, a):
        if len(a) <= 1:
            return a, 0
        mid = len(a) // 2
        left, x = self._sort(a[:mid])
        right, y = self._sort(a[mid:])
        merged = []
        i = j = 0
        inv = x + y
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
                inv += len(left) - i
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged, inv

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    scores = list(map(int, data[1:1 + n]))
    print(Solution().countInversions(scores))

if __name__ == "__main__":
    main()

"""
Approach: Merge sort; while merging, when a right-side value is strictly smaller than the remaining left-side values, all of those form inversions.
Time Complexity : O(n log n)
Auxiliary Space : O(n)
"""
