import sys

class Solution:
    def feasible(self, pages, m, limit):
        groups = 1
        cur = 0
        for p in pages:
            if cur + p > limit:
                groups += 1
                cur = 0
            cur += p
        return groups <= m

    def minMaxPages(self, pages, m):
        if m > len(pages):
            return -1
        lo = 0
        hi = 0
        for p in pages:
            if p > lo:
                lo = p
            hi += p
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if self.feasible(pages, m, mid):
                hi = mid
            else:
                lo = mid + 1
        return lo

def main():
    data = sys.stdin.read().split()
    n, m = int(data[0]), int(data[1])
    pages = list(map(int, data[2:2 + n]))
    print(Solution().minMaxPages(pages, m))

if __name__ == "__main__":
    main()

"""
Approach: Binary search on the answer: the smallest limit between the largest book and the total pages for which a greedy split uses at most m groups.
Time Complexity : O(n * log(sum of pages))
Auxiliary Space : O(1)
"""
