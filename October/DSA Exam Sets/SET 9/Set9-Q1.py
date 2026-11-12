import sys

class Solution:
    def twoSumSorted(self, prices, T):
        i, j = 0, len(prices) - 1
        while i < j:
            s = prices[i] + prices[j]
            if s == T:
                return i + 1, j + 1
            elif s < T:
                i += 1
            else:
                j -= 1

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    prices = list(map(int, data[1:1 + n]))
    T = int(data[1 + n])
    i, j = Solution().twoSumSorted(prices, T)
    print(i, j)

if __name__ == "__main__":
    main()

"""
Approach: Two pointers from both ends of the sorted list; move the left pointer up if the sum is too small, the right pointer down if too large.
Time Complexity : O(n)
Auxiliary Space : O(1)
"""
