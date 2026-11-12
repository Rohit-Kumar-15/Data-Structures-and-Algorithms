import sys

class Solution:
    def feasible(self, weights, D, cap):
        days = 1
        cur = 0
        for w in weights:
            if cur + w > cap:
                days += 1
                cur = 0
            cur += w
        return days <= D

    def minCapacity(self, weights, D):
        lo = 0
        hi = 0
        for w in weights:
            if w > lo:
                lo = w
            hi += w
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if self.feasible(weights, D, mid):
                hi = mid
            else:
                lo = mid + 1
        return lo

def main():
    data = sys.stdin.read().split()
    n, D = int(data[0]), int(data[1])
    weights = list(map(int, data[2:2 + n]))
    print(Solution().minCapacity(weights, D))

if __name__ == "__main__":
    main()

"""
Approach: Binary search on the answer. Capacity ranges from the heaviest package to the total weight; a capacity is feasible if a greedy loading uses at most D days.
Time Complexity : O(n * log(sum of weights))
Auxiliary Space : O(1)
"""
