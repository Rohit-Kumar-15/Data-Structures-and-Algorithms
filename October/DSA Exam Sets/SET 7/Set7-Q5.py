import sys

class Solution:
    def findInMountain(self, a, h):
        n = len(a)
        lo, hi = 0, n - 1
        while lo < hi:                       # find the peak
            mid = lo + (hi - lo) // 2
            if a[mid] < a[mid + 1]:
                lo = mid + 1
            else:
                hi = mid
        peak = lo

        lo, hi = 0, peak                     # ascending part
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if a[mid] == h:
                return mid
            elif a[mid] < h:
                lo = mid + 1
            else:
                hi = mid - 1

        lo, hi = peak + 1, n - 1             # descending part
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if a[mid] == h:
                return mid
            elif a[mid] > h:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    a = list(map(int, data[1:1 + n]))
    h = int(data[1 + n])
    print(Solution().findInMountain(a, h))

if __name__ == "__main__":
    main()

"""
Approach: Binary search for the peak, then binary search the ascending part; only if not found, binary search the descending part. Checking the ascending part first gives the smallest index.
Time Complexity : O(log n)
Auxiliary Space : O(1)
"""
