import sys

class Solution:
    def hasNearDuplicate(self, ids, k):
        last = {}
        for i, x in enumerate(ids):
            if x in last and i - last[x] <= k:
                return True
            last[x] = i
        return False

def main():
    data = sys.stdin.read().split()
    n, k = int(data[0]), int(data[1])
    ids = list(map(int, data[2:2 + n]))
    print("YES" if Solution().hasNearDuplicate(ids, k) else "NO")

if __name__ == "__main__":
    main()

"""
Approach: Remember the last position of each ID in a dictionary; alert if the same ID reappears within k positions.
Time Complexity : O(n)
Auxiliary Space : O(n)
"""
