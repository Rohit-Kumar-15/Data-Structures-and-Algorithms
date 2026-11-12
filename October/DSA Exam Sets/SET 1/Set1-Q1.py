import sys

class Solution:
    def twoSum(self, prices, T):
        seen = {}
        for j, p in enumerate(prices):
            if T - p in seen:
                return seen[T - p], j
            seen[p] = j

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    prices = list(map(int, data[1:1 + n]))
    T = int(data[1 + n])
    i, j = Solution().twoSum(prices, T)
    print(i, j)

if __name__ == "__main__":
    main()

"""
Approach: Store each price's index in a hash map. For each position j, check whether T - price[j] was already seen.
Time Complexity : O(n)
Auxiliary Space : O(n)
"""
