import sys

class Solution:
    def commonIds(self, A, B):
        setA = set(A)
        seen = set()
        common = []
        for x in B:
            if x in setA and x not in seen:
                seen.add(x)
                common.append(x)
        return self.mergeSort(common)

    def mergeSort(self, a):
        if len(a) <= 1:
            return a
        mid = len(a) // 2
        left = self.mergeSort(a[:mid])
        right = self.mergeSort(a[mid:])
        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i]); i += 1
            else:
                merged.append(right[j]); j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged

def main():
    data = sys.stdin.read().split()
    m, n = int(data[0]), int(data[1])
    A = list(map(int, data[2:2 + m]))
    B = list(map(int, data[2 + m:2 + m + n]))
    res = Solution().commonIds(A, B)
    print(" ".join(map(str, res)) if res else "None")

if __name__ == "__main__":
    main()

"""
Approach: Put sheet A in a hash set; collect each distinct ID of B found in it; sort the result with merge sort.
Time Complexity : O(m + n + k log k), k = number of common IDs
Auxiliary Space : O(m + n)
"""
