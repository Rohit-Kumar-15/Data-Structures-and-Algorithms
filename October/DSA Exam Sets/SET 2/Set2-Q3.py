import sys

class Solution:
    def longestStreak(self, arr, T):
        best = 0
        cur = 0
        for x in arr:
            if x >= T:
                cur += 1
                if cur > best:
                    best = cur
            else:
                cur = 0
        return best

def main():
    data = sys.stdin.read().split()
    n, T = int(data[0]), int(data[1])
    arr = list(map(int, data[2:2 + n]))
    print(Solution().longestStreak(arr, T))

if __name__ == "__main__":
    main()

"""
Approach: Walk the array counting consecutive days with attendance >= T; reset the count on any day below T.
Time Complexity : O(n)
Auxiliary Space : O(1)
"""
