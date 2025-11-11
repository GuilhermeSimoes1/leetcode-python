class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:

        sub = ""
        for x in s:

            sub += x

            if len(sub) > len(s) / 2:
                return False

            if len(s) % len(sub) == 0:
                res = sub * int((len(s) / len(sub)))
                if res == s:
                    return True

        return False










