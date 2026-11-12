import sys

class Solution:
    def maxWindow(self, arr, k):
        window = sum_first = 0
        for i in range(k):
            window += arr[i]
        best = window
        for i in range(k, len(arr)):
            window += arr[i] - arr[i - k]
            if window > best:
                best = window
        return best

def main():
    data = sys.stdin.read().split()
    n, k = int(data[0]), int(data[1])
    arr = list(map(int, data[2:2 + n]))
    print(Solution().maxWindow(arr, k))

if __name__ == "__main__":
    main()

"""
Approach: Sum the first k values, then slide the window by adding the entering value and removing the leaving one.
Time Complexity : O(n)
Auxiliary Space : O(1)
"""
