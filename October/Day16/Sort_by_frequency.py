class Solution:
    def frequencySort(self, s: str) -> str:
        charfreq = {}

        for char in s:
            if char not in charfreq:
                charfreq[char] = 1
            else:
                charfreq[char] += 1

        chars = list(charfreq.keys())

        for i in range(len(chars)):
            largest = i

            for j in range(i + 1, len(chars)):
                if charfreq[chars[j]] > charfreq[chars[largest]]:
                    largest = j

            chars[i], chars[largest] = chars[largest], chars[i]

        res = ""
        for char in chars:
            res += char * charfreq[char]

        return res

"""
first we make a dictionary and store the characters and their frequency
next we sort a list of keys based on descending order of its frequency using data from the dictionary
next we make a string with element in descending order of frequency

Time Complexity: O(n^2)
Space Complexity: O(n)
"""