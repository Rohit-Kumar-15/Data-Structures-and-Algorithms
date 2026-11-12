import sys

class Solution:
    def quickSort3Way(self, a):
        stack = [(0, len(a) - 1)]
        while stack:
            lo, hi = stack.pop()
            if lo >= hi:
                continue
            pivot = a[(lo + hi) // 2]
            lt, i, gt = lo, lo, hi
            while i <= gt:
                if a[i] < pivot:
                    a[lt], a[i] = a[i], a[lt]
                    lt += 1
                    i += 1
                elif a[i] > pivot:
                    a[i], a[gt] = a[gt], a[i]
                    gt -= 1
                else:
                    i += 1
            stack.append((lo, lt - 1))
            stack.append((gt + 1, hi))
        return a

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    a = list(map(int, data[1:1 + n]))
    print(" ".join(map(str, Solution().quickSort3Way(a))))

if __name__ == "__main__":
    main()

"""
Approach: Iterative quicksort with 3-way partitioning on the middle element. Equal elements are grouped and skipped; an explicit stack holds the ranges still to sort.
Time Complexity : O(n log n) average, degrades with many distinct values only in theory; with few distinct values it is about O(n)
Auxiliary Space : O(log n) stack on average
"""
