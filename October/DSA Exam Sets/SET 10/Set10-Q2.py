import sys

class Solution:
    def floorCeil(self, a, q):
        n = len(a)
        floor = None
        lo, hi = 0, n - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if a[mid] <= q:
                floor = a[mid]
                lo = mid + 1
            else:
                hi = mid - 1
        ceil = None
        lo, hi = 0, n - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if a[mid] >= q:
                ceil = a[mid]
                hi = mid - 1
            else:
                lo = mid + 1
        return floor, ceil

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    a = list(map(int, data[1:1 + n]))
    q = int(data[1 + n])
    f, c = Solution().floorCeil(a, q)
    print("None" if f is None else f, "None" if c is None else c)

if __name__ == "__main__":
    main()

"""
Approach: Two binary searches: the last value <= q gives the floor, the first value >= q gives the ceiling.
Time Complexity : O(log n)
Auxiliary Space : O(1)
"""
