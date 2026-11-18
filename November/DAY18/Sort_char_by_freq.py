class Solution:
    def sortbyfrequency(self, s: str) -> str:
        freq = {}
        for k in s:
            if k not in freq:
                freq[k] = 1
            else:
                freq[k] += 1

        chars = list(freq.keys())

        for i in range (len(chars)):
            largest = i
            for j in range(i+1, len(chars)):
                if freq[chars[j]] > freq[chars[largest]]:
                    largest = j
            chars[i], chars[largest] = chars[largest], chars[i]

        res = ""
        for i in chars:
            res += i*freq[i]

        return res

"""
first we make a dictionary and store the characters and their frequency
next we sort a list of keys based on descending order of its frequency using data from the dictionary
next we make a string with element in descending order of frequency

Time Complexity: O(n^2)
Space Complexity: O(n)
"""
