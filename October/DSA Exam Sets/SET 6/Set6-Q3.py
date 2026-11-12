import sys

class Solution:
    def union(self, A, B):
        i = j = 0
        res = []
        while i < len(A) and j < len(B):
            if A[i] < B[j]:
                res.append(A[i]); i += 1
            elif A[i] > B[j]:
                res.append(B[j]); j += 1
            else:
                res.append(A[i]); i += 1; j += 1
        res.extend(A[i:])
        res.extend(B[j:])
        return res

def main():
    data = sys.stdin.read().split()
    m, n = int(data[0]), int(data[1])
    A = list(map(int, data[2:2 + m]))
    B = list(map(int, data[2 + m:2 + m + n]))
    print(" ".join(map(str, Solution().union(A, B))))

if __name__ == "__main__":
    main()

"""
Approach: Two-pointer merge of the sorted lists; when values are equal, output once and advance both pointers.
Time Complexity : O(m + n)
Auxiliary Space : O(m + n) for the output
"""
