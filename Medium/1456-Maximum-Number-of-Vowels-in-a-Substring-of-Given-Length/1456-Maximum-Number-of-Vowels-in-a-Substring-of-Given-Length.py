class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        dic = {
            "a",
            "e",
            "i",
            "o",
            "u"
        }

        maxVowel = 0
        count = 0

        for i in range(k):
            if s[i] in dic:
                count += 1

        maxVowel = count

        for i in range(k, len(s)):
            if s[i] in dic:
                count += 1
            if s[i - k] in dic:
                count -= 1

            maxVowel = max(maxVowel, count)
        return maxVowel




