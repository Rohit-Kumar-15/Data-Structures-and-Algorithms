import sys

class Solution:
    def moveZeros(self, a):
        w = 0
        for x in a:
            if x != 0:
                a[w] = x
                w += 1
        for k in range(w, len(a)):
            a[k] = 0
        return a

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    a = list(map(int, data[1:1 + n]))
    print(" ".join(map(str, Solution().moveZeros(a))))

if __name__ == "__main__":
    main()

"""
Approach: Copy every non-zero value forward to a write index in one pass, then fill the remaining slots with zeros.
Time Complexity : O(n)
Auxiliary Space : O(1)
"""
