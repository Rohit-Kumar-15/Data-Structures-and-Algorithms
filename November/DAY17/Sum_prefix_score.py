
class Solution:
    def sumPrefixScores(self, words):
        freq = {}

        for word in words:
            prefix = ""

            for ch in word:
                prefix += ch
                freq[prefix] = freq.get(prefix, 0) + 1

        result = []

        for word in words:
            score = 0
            prefix = ""

            for ch in word:
                prefix += ch
                score += freq[prefix]

            result.append(score)

        return result
