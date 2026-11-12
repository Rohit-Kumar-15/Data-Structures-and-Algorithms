import sys

class Solution:
    def firstOne(self, a):
        lo, hi = 0, len(a) - 1
        ans = -1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if a[mid] == 1:
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return ans + 1 if ans != -1 else -1

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    a = list(map(int, data[1:1 + n]))
    print(Solution().firstOne(a))

if __name__ == "__main__":
    main()

"""
Approach: Binary search for the leftmost 1; when a 1 is found, record it and keep searching to the left.
Time Complexity : O(log n)
Auxiliary Space : O(1)
"""
