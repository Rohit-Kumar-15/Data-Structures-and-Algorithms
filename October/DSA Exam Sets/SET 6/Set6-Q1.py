import sys

class Solution:
    def countingSort(self, marks):
        counts = [0] * 101
        for m in marks:
            counts[m] += 1
        result = []
        for value in range(101):
            result.extend([value] * counts[value])
        return result

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    marks = list(map(int, data[1:1 + n]))
    print(" ".join(map(str, Solution().countingSort(marks))))

if __name__ == "__main__":
    main()

"""
Approach: Counting sort: count occurrences of each mark 0..100, then write each value out count times.
Time Complexity : O(n + 101)
Auxiliary Space : O(1) extra for the count array (plus output)
"""
