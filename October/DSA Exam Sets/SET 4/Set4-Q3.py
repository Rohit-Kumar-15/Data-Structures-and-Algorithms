import sys

class Solution:
    def countWindows(self, arr, k, T):
        window = 0
        for i in range(k):
            window += arr[i]
        count = 1 if window >= k * T else 0
        for i in range(k, len(arr)):
            window += arr[i] - arr[i - k]
            if window >= k * T:
                count += 1
        return count

def main():
    data = sys.stdin.read().split()
    n, k, T = int(data[0]), int(data[1]), int(data[2])
    arr = list(map(int, data[3:3 + n]))
    print(Solution().countWindows(arr, k, T))

if __name__ == "__main__":
    main()

"""
Approach: Slide a window of size k keeping its sum, and count windows whose sum is at least k*T.
Time Complexity : O(n)
Auxiliary Space : O(1)
"""
