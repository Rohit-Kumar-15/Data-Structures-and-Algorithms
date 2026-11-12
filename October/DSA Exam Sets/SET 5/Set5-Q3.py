import sys

class Solution:
    def insertionSort(self, a):
        shifts = 0
        for i in range(1, len(a)):
            key = a[i]
            j = i - 1
            while j >= 0 and a[j] > key:
                a[j + 1] = a[j]
                shifts += 1
                j -= 1
            a[j + 1] = key
        return a, shifts

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    a = list(map(int, data[1:1 + n]))
    arr, shifts = Solution().insertionSort(a)
    print(" ".join(map(str, arr)))
    print(shifts)

if __name__ == "__main__":
    main()

"""
Approach: Insertion sort; each element is moved left past every larger element, and each one-place move is counted as a shift.
Time Complexity : O(n^2) worst case, O(n) on nearly sorted input
Auxiliary Space : O(1)
"""
