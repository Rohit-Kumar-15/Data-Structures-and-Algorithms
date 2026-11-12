import sys

class Solution:
    def secondDistinct(self, arr):
        first = None
        second = None
        for x in arr:
            if first is None or x > first:
                if first is not None:
                    second = first
                first = x
            elif x != first and (second is None or x > second):
                second = x
        return second

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    arr = list(map(int, data[1:1 + n]))
    res = Solution().secondDistinct(arr)
    print("None" if res is None else res)

if __name__ == "__main__":
    main()

"""
Approach: Track the largest and second-largest distinct values in one pass, ignoring values equal to the current largest.
Time Complexity : O(n)
Auxiliary Space : O(1)
"""
