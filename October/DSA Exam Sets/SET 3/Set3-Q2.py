import sys

class Solution:
    def reverseVowels(self, s):
        vowels = set("aeiouAEIOU")
        s = list(s)
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] not in vowels:
                l += 1
            elif s[r] not in vowels:
                r -= 1
            else:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
        return "".join(s)

def main():
    s = sys.stdin.readline().rstrip("\n")
    print(Solution().reverseVowels(s))

if __name__ == "__main__":
    main()

"""
Approach: Two pointers from both ends; skip consonants and swap when both pointers sit on vowels.
Time Complexity : O(n)
Auxiliary Space : O(n) for the character list
"""
