import sys

class Solution:
    def floorSqrt(self, x):
        lo, hi = 0, x
        ans = 0
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if mid * mid <= x:
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans

def main():
    x = int(sys.stdin.readline().strip())
    print(Solution().floorSqrt(x))

if __name__ == "__main__":
    main()

"""
Approach: Binary search over candidate side lengths s in [0, x] for the largest s with s*s <= x.
Time Complexity : O(log x)
Auxiliary Space : O(1)
"""
