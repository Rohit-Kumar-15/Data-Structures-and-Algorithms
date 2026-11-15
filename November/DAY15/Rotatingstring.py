class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        return goal in (s + s)

"""
If goal is not equal to string then false else just check if the goal is present in string 

Time Complexity: O(1)
Space Complexity: O(1)
"""