import sys

class Solution:
    def isPalindrome(self, s):
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True

def main():
    s = sys.stdin.readline().rstrip("\n")
    print("YES" if Solution().isPalindrome(s) else "NO")

if __name__ == "__main__":
    main()

"""
Approach: Two pointers moving inward from both ends, skipping non-alphanumeric characters and comparing letters case-insensitively.
Time Complexity : O(n)
Auxiliary Space : O(1)
"""
