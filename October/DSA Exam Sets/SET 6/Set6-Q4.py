import sys

class Solution:
    def sortByFrequency(self, ids):
        freq = {}
        for x in ids:
            freq[x] = freq.get(x, 0) + 1
        distinct = list(freq.keys())

        def before(a, b):
            if freq[a] != freq[b]:
                return freq[a] < freq[b]
            return a > b

        # insertion sort on the distinct IDs using the custom comparison
        for i in range(1, len(distinct)):
            key = distinct[i]
            j = i - 1
            while j >= 0 and before(key, distinct[j]):
                distinct[j + 1] = distinct[j]
                j -= 1
            distinct[j + 1] = key

        result = []
        for x in distinct:
            result.extend([x] * freq[x])
        return result

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    ids = list(map(int, data[1:1 + n]))
    print(" ".join(map(str, Solution().sortByFrequency(ids))))

if __name__ == "__main__":
    main()

"""
Approach: Count frequencies, sort the distinct IDs with a custom comparison (lower frequency first, then larger ID first), and expand each ID by its count.
Time Complexity : O(n + d^2), where d is the number of distinct IDs
Auxiliary Space : O(n)
"""
