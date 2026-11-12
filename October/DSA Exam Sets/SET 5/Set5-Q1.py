import sys

class Solution:
    def bubbleSort(self, a):
        passes = 0
        n = len(a)
        for end in range(n - 1, 0, -1):
            swapped = False
            for j in range(end):
                if a[j] > a[j + 1]:
                    a[j], a[j + 1] = a[j + 1], a[j]
                    swapped = True
            if not swapped:
                break
            passes += 1
        return a, passes

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    a = list(map(int, data[1:1 + n]))
    arr, passes = Solution().bubbleSort(a)
    print(" ".join(map(str, arr)))
    print(passes)

if __name__ == "__main__":
    main()

"""
Approach: Bubble sort; each pass pushes the largest remaining value to the end. Count passes that performed at least one swap.
Time Complexity : O(n^2)
Auxiliary Space : O(1)
"""
