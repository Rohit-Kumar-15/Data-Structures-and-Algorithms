
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        m = 0

        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                profit = prices[j] - prices[i]

                if profit > m:
                    m = profit

        return m

"""
run a nested loop and calculate the profit of all days if profit is greater then save and return at last

Time Complexity: O(n^2)
"""