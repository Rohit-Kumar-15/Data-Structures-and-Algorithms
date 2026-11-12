import sys

class Solution:
    def sortTags(self, a):
        lo, mid, hi = 0, 0, len(a) - 1
        while mid <= hi:
            if a[mid] == 0:
                a[lo], a[mid] = a[mid], a[lo]
                lo += 1
                mid += 1
            elif a[mid] == 2:
                a[mid], a[hi] = a[hi], a[mid]
                hi -= 1
            else:
                mid += 1
        return a

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    a = list(map(int, data[1:1 + n]))
    print(" ".join(map(str, Solution().sortTags(a))))

if __name__ == "__main__":
    main()

"""
Approach: Dutch national flag with three pointers: lo marks the end of 0s, mid scans, hi marks the start of 2s.
Time Complexity : O(n)
Auxiliary Space : O(1)
"""
