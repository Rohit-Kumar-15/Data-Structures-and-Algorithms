import sys

class Solution:
    def longestUnique(self, codes):
        last = {}
        left = 0
        best = 0
        for i, x in enumerate(codes):
            if x in last and last[x] >= left:
                left = last[x] + 1
            last[x] = i
            if i - left + 1 > best:
                best = i - left + 1
        return best

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    codes = list(map(int, data[1:1 + n]))
    print(Solution().longestUnique(codes))

if __name__ == "__main__":
    main()

"""
Approach: Sliding window with a dictionary of last seen positions; when a repeat appears inside the window, move the left edge past its previous occurrence.
Time Complexity : O(n)
Auxiliary Space : O(n)
"""
