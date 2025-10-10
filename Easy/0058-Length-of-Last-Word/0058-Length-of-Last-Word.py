class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        word = ""
        s = s.strip()

        for i in range(len(s)):
            word += s[i]
            if s[i] == " ":
                word = ""
        return len(word)
