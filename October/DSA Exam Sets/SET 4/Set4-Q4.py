import sys

class Solution:
    def findAnagrams(self, s, p):
        m, n = len(p), len(s)
        res = []
        if m > n:
            return res
        pc = [0] * 26
        wc = [0] * 26
        for c in p:
            pc[ord(c) - 97] += 1
        for i in range(n):
            wc[ord(s[i]) - 97] += 1
            if i >= m:
                wc[ord(s[i - m]) - 97] -= 1
            if i >= m - 1 and wc == pc:
                res.append(i - m + 1)
        return res

def main():
    s = sys.stdin.readline().strip()
    p = sys.stdin.readline().strip()
    res = Solution().findAnagrams(s, p)
    print(" ".join(map(str, res)) if res else "None")

if __name__ == "__main__":
    main()

"""
Approach: Sliding window of length |p| with a 26-letter count array; the window is an anagram when its counts equal those of p.
Time Complexity : O(26 * (|s|)) = O(|s|)
Auxiliary Space : O(1)
"""
