import sys

class Solution:
    def search(self, a, q):
        lo, hi = 0, len(a) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if a[mid] == q:
                return mid
            elif a[mid] < q:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    a = list(map(int, data[1:1 + n]))
    q = int(data[1 + n])
    print(Solution().search(a, q))

if __name__ == "__main__":
    main()

"""
Approach: Classic binary search on a strictly increasing array.
Time Complexity : O(log n)
Auxiliary Space : O(1)
"""
