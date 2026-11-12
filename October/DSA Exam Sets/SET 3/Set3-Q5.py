import sys

class Solution:
    def keepTwo(self, a):
        w = 0
        for x in a:
            if w < 2 or x != a[w - 2]:
                a[w] = x
                w += 1
        return w

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    a = list(map(int, data[1:1 + n]))
    k = Solution().keepTwo(a)
    print(k)
    print(" ".join(map(str, a[:k])))

if __name__ == "__main__":
    main()

"""
Approach: Write pointer w. A value is kept if w < 2 or it differs from the value two slots before w (which guarantees at most two copies).
Time Complexity : O(n)
Auxiliary Space : O(1)
"""
