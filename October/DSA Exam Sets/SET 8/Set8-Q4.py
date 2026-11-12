import sys

class Solution:
    def searchRotated(self, a, t):
        lo, hi = 0, len(a) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if a[mid] == t:
                return mid
            if a[lo] <= a[mid]:                       # left half sorted
                if a[lo] <= t < a[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:                                      # right half sorted
                if a[mid] < t <= a[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return -1

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    a = list(map(int, data[1:1 + n]))
    t = int(data[1 + n])
    print(Solution().searchRotated(a, t))

if __name__ == "__main__":
    main()

"""
Approach: Modified binary search: at each step one half is sorted; check whether the target lies inside that sorted half and discard the other.
Time Complexity : O(log n)
Auxiliary Space : O(1)
"""
