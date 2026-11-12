import sys

class Solution:
    def lowerBound(self, a, x):
        lo, hi = 0, len(a)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if a[mid] < x:
                lo = mid + 1
            else:
                hi = mid
        return lo

    def upperBound(self, a, x):
        lo, hi = 0, len(a)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if a[mid] <= x:
                lo = mid + 1
            else:
                hi = mid
        return lo

    def firstLast(self, a, x):
        first = self.lowerBound(a, x)
        if first == len(a) or a[first] != x:
            return -1, -1
        return first, self.upperBound(a, x) - 1

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    a = list(map(int, data[1:1 + n]))
    x = int(data[1 + n])
    f, l = Solution().firstLast(a, x)
    print(f, l)

if __name__ == "__main__":
    main()

"""
Approach: Two binary searches: lower bound gives the first occurrence; upper bound minus one gives the last occurrence.
Time Complexity : O(log n)
Auxiliary Space : O(1)
"""
