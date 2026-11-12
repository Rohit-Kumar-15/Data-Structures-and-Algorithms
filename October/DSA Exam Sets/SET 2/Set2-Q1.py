import sys

class Solution:
    def majority(self, ids):
        counts = {}
        for x in ids:
            counts[x] = counts.get(x, 0) + 1
            if counts[x] > len(ids) // 2:
                return x

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    ids = list(map(int, data[1:1 + n]))
    print(Solution().majority(ids))

if __name__ == "__main__":
    main()

"""
Approach: Count occurrences in a dictionary and return the ID whose count first exceeds n/2.
Time Complexity : O(n)
Auxiliary Space : O(n)
"""
