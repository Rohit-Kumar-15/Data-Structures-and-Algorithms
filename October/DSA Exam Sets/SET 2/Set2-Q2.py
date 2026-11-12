import sys

class Solution:
    def firstUnique(self, ids):
        counts = {}
        for x in ids:
            counts[x] = counts.get(x, 0) + 1
        for x in ids:
            if counts[x] == 1:
                return x
        return -1

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    ids = list(map(int, data[1:1 + n]))
    print(Solution().firstUnique(ids))

if __name__ == "__main__":
    main()

"""
Approach: Count every ID in a first pass, then scan the log again and return the first ID with count 1.
Time Complexity : O(n)
Auxiliary Space : O(n)
"""
