class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        finalWord = ""
        for x, y in zip_longest(word1, word2, fillvalue=""):
            finalWord += x
            finalWord += y

        return finalWord