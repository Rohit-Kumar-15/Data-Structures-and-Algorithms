class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        news = s*2
        n = len(news)
        g = len(goal)

        for i in range(0, n-g+1):
            j = 0
            while j<g and news[i+j] == goal[j]:
                j += 1
            
            if j == g:
                return True
        return False

"""
First we double the string then use the sliding window approach when we encounter the char equal to first char in 
needle we check if the subsequient characters are equal as well

Time Complexity: O(n)
Space Complexity: O(1)
"""