import sys

class Solution:
    def merge(self, A, m, B, n):
        i, j, k = m - 1, n - 1, m + n - 1
        while j >= 0:
            if i >= 0 and A[i] > B[j]:
                A[k] = A[i]
                i -= 1
            else:
                A[k] = B[j]
                j -= 1
            k -= 1
        return A

def main():
    data = sys.stdin.read().split()
    m, n = int(data[0]), int(data[1])
    A = list(map(int, data[2:2 + m + n]))
    B = list(map(int, data[2 + m + n:2 + m + 2 * n]))
    print(" ".join(map(str, Solution().merge(A, m, B, n))))

if __name__ == "__main__":
    main()

"""
Approach: Fill A from the back with the largest remaining value of A or B, so no unread value of A is overwritten.
Time Complexity : O(m + n)
Auxiliary Space : O(1)
"""
