import sys

class Solution:
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0
        min_price = prices[0]
        best = 0
        for p in prices[1:]:
            if p - min_price > best:
                best = p - min_price
            if p < min_price:
                min_price = p
        return best

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    prices = list(map(int, data[1:1 + n]))
    print(Solution().maxProfit(prices))

if __name__ == "__main__":
    main()

"""
Approach: Track the lowest price seen so far; at each day, the best sale is today's price minus that low.
Time Complexity : O(n)
Auxiliary Space : O(1)
"""
