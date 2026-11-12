import sys

class Solution:
    def smallestK(self, times, k):
        a = list(times)
        n = len(a)
        result = []
        for r in range(k):
            min_idx = r
            for j in range(r + 1, n):
                if a[j] < a[min_idx]:
                    min_idx = j
            a[r], a[min_idx] = a[min_idx], a[r]
            result.append(a[r])
        return result

def main():
    data = sys.stdin.read().split()
    n, k = int(data[0]), int(data[1])
    times = list(map(int, data[2:2 + n]))
    print(" ".join(map(str, Solution().smallestK(times, k))))

if __name__ == "__main__":
    main()

"""
Approach: Run k rounds of selection sort; each round moves the minimum of the unsorted part to the front.
Time Complexity : O(n * k)
Auxiliary Space : O(n) for the copy
"""
