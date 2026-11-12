import sys

class Solution:
    def reverse(self, a, i, j):
        while i < j:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1

    def rotateRight(self, a, k):
        n = len(a)
        k %= n
        self.reverse(a, 0, n - 1)
        self.reverse(a, 0, k - 1)
        self.reverse(a, k, n - 1)
        return a

def main():
    data = sys.stdin.read().split()
    n, k = int(data[0]), int(data[1])
    a = list(map(int, data[2:2 + n]))
    print(" ".join(map(str, Solution().rotateRight(a, k))))

if __name__ == "__main__":
    main()

"""
Approach: Reverse the whole array, then reverse the first k and the remaining n-k elements separately (reversal trick), all with explicit swaps.
Time Complexity : O(n)
Auxiliary Space : O(1)
"""
