import sys

class Solution:
    def insert(self, intervals, new):
        s, e = new
        result = []
        i = 0
        n = len(intervals)
        while i < n and intervals[i][1] < s:
            result.append(intervals[i])
            i += 1
        while i < n and intervals[i][0] <= e:
            s = min_val(s, intervals[i][0])
            e = max_val(e, intervals[i][1])
            i += 1
        result.append([s, e])
        while i < n:
            result.append(intervals[i])
            i += 1
        return result

def min_val(a, b):
    return a if a < b else b

def max_val(a, b):
    return a if a > b else b

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    intervals = []
    for i in range(n):
        intervals.append([int(data[1 + 2 * i]), int(data[2 + 2 * i])])
    pos = 1 + 2 * n
    new = [int(data[pos]), int(data[pos + 1])]
    for s, e in Solution().insert(intervals, new):
        print(s, e)

if __name__ == "__main__":
    main()

"""
Approach: Copy intervals ending before the new one, merge all intervals that overlap or touch it, then copy the rest.
Time Complexity : O(n)
Auxiliary Space : O(n)
"""
