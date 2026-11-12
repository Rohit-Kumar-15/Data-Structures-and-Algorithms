import sys

class Solution:
    def rangeSums(self, sales, queries):
        prefix = [0] * (len(sales) + 1)
        for i in range(len(sales)):
            prefix[i + 1] = prefix[i] + sales[i]
        return [prefix[r + 1] - prefix[l] for l, r in queries]

def main():
    data = sys.stdin.read().split()
    n, q = int(data[0]), int(data[1])
    sales = list(map(int, data[2:2 + n]))
    pos = 2 + n
    queries = []
    for _ in range(q):
        queries.append((int(data[pos]), int(data[pos + 1])))
        pos += 2
    print("\n".join(map(str, Solution().rangeSums(sales, queries))))

if __name__ == "__main__":
    main()

"""
Approach: Build a prefix-sum array once; each query sum(l..r) = prefix[r+1] - prefix[l].
Time Complexity : O(n + q)
Auxiliary Space : O(n)
"""
