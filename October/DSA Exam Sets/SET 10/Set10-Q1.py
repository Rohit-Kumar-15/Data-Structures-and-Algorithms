import sys

class Solution:
    def sortedSquares(self, a):
        n = len(a)
        res = [0] * n
        lo, hi = 0, n - 1
        for k in range(n - 1, -1, -1):
            if abs(a[lo]) > abs(a[hi]):
                res[k] = a[lo] * a[lo]
                lo += 1
            else:
                res[k] = a[hi] * a[hi]
                hi -= 1
        return res

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    a = list(map(int, data[1:1 + n]))
    print(" ".join(map(str, Solution().sortedSquares(a))))

if __name__ == "__main__":
    main()

"""
Approach: Two pointers from both ends; the larger absolute value is the next largest square, filled from the back of the result.
Time Complexity : O(n)
Auxiliary Space : O(n) for the output
"""
