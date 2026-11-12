import sys

class Solution:
    def threeSum(self, a):
        a = self.mergeSort(a)
        n = len(a)
        res = []
        for i in range(n - 2):
            if i > 0 and a[i] == a[i - 1]:
                continue
            l, r = i + 1, n - 1
            while l < r:
                s = a[i] + a[l] + a[r]
                if s == 0:
                    res.append((a[i], a[l], a[r]))
                    l += 1
                    while l < r and a[l] == a[l - 1]:
                        l += 1
                elif s < 0:
                    l += 1
                else:
                    r -= 1
        return res

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
    n = int(data[0])
    a = list(map(int, data[1:1 + n]))
    res = Solution().threeSum(a)
    if not res:
        print("None")
    for x, y, z in res:
        print(x, y, z)

if __name__ == "__main__":
    main()

"""
Approach: Sort the values, fix the first element of each triplet (skipping repeated values), and use two pointers on the rest; skipping repeated values yields distinct triplets in lexicographic order.
Time Complexity : O(n^2)
Auxiliary Space : O(n) for the sort
"""
