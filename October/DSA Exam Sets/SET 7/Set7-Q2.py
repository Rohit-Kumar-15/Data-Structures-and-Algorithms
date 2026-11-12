import sys

class Solution:
    def searchInsert(self, a, t):
        lo, hi = 0, len(a)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if a[mid] < t:
                lo = mid + 1
            else:
                hi = mid
        return lo

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    a = list(map(int, data[1:1 + n]))
    t = int(data[1 + n])
    print(Solution().searchInsert(a, t))

if __name__ == "__main__":
    main()

"""
Approach: Lower-bound binary search: find the first index whose value is >= t. That index is t's position if present, or the insertion point otherwise.
Time Complexity : O(log n)
Auxiliary Space : O(1)
"""
