import sys

class Solution:
    def trimmedMean(self, scores, t):
        counts = [0] * 101
        for s in scores:
            counts[s] += 1
        ordered = []
        for v in range(101):
            ordered.extend([v] * counts[v])
        kept = ordered[t:len(ordered) - t]
        return sum_list(kept) / len(kept)

def sum_list(a):
    total = 0
    for x in a:
        total += x
    return total

def main():
    data = sys.stdin.read().split()
    n, t = int(data[0]), int(data[1])
    scores = list(map(int, data[2:2 + n]))
    print("%.2f" % Solution().trimmedMean(scores, t))

if __name__ == "__main__":
    main()

"""
Approach: Sort the scores with counting sort (scores are 0..100), drop the t lowest and t highest, and average the rest.
Time Complexity : O(n + 101)
Auxiliary Space : O(n)
"""
