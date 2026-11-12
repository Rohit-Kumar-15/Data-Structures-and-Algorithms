import sys

class Solution:
    def firstRepeat(self, ids):
        seen = set()
        for x in ids:
            if x in seen:
                return x
            seen.add(x)
        return -1

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    ids = list(map(int, data[1:1 + n]))
    print(Solution().firstRepeat(ids))

if __name__ == "__main__":
    main()

"""
Approach: Scan left to right with a set of seen IDs; the first ID already in the set is the answer.
Time Complexity : O(n)
Auxiliary Space : O(n)
"""
