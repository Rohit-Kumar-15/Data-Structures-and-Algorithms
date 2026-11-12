import sys

class Solution:
    def findMin(self, a):
        lo, hi = 0, len(a) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if a[mid] > a[hi]:
                lo = mid + 1
            else:
                hi = mid
        return a[lo]

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    a = list(map(int, data[1:1 + n]))
    print(Solution().findMin(a))

if __name__ == "__main__":
    main()

"""
Approach: If the middle value is greater than the rightmost value, the minimum lies to its right; otherwise it is at mid or to its left.
Time Complexity : O(log n)
Auxiliary Space : O(1)
"""
