import sys

class Solution:
    def searchMatrix(self, matrix, R, C, t):
        lo, hi = 0, R * C - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            val = matrix[mid // C][mid % C]
            if val == t:
                return mid // C, mid % C
            elif val < t:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1, -1

def main():
    data = sys.stdin.read().split()
    R, C = int(data[0]), int(data[1])
    pos = 2
    matrix = []
    for _ in range(R):
        matrix.append(list(map(int, data[pos:pos + C])))
        pos += C
    t = int(data[pos])
    r, c = Solution().searchMatrix(matrix, R, C, t)
    print(r, c)

if __name__ == "__main__":
    main()

"""
Approach: Treat the matrix as a sorted 1-D array of R*C values and binary search it, converting each index with row = idx // C and col = idx % C.
Time Complexity : O(log(R*C))
Auxiliary Space : O(1)
"""
