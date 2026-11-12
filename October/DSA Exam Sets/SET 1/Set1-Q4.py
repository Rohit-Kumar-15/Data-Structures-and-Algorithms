import sys

class Solution:
    def balancePoint(self, arr):
        total = 0
        for x in arr:
            total += x
        left = 0
        for p in range(len(arr)):
            right = total - left - arr[p]
            if left == right:
                return p
            left += arr[p]
        return -1

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    arr = list(map(int, data[1:1 + n]))
    print(Solution().balancePoint(arr))

if __name__ == "__main__":
    main()

"""
Approach: Compute the total once, then sweep left to right keeping the running left sum. Right sum = total - left - arr[p].
Time Complexity : O(n)
Auxiliary Space : O(1)
"""
