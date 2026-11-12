import sys

class Solution:
    def missingNumbers(self, n, arr):
        present = set(arr)
        return [k for k in range(1, n + 1) if k not in present]

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    arr = list(map(int, data[1:1 + n]))
    res = Solution().missingNumbers(n, arr)
    print(" ".join(map(str, res)) if res else "None")

if __name__ == "__main__":
    main()

"""
Approach: Put the sheet entries in a set, then list every roll number 1..n that is not in the set.
Time Complexity : O(n)
Auxiliary Space : O(n)
"""
