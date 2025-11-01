class Solution:
    def firstUniqChar(self, s: str) -> int:

        res = -1

        if len(s) == 1:
            return 0

        for i in range(len(s)):

            if res != -1:
                return res
            else:
                for z in range(len(s)):

                    if i != z:
                        if s[i] == s[z]:
                            res = -1
                            break
                        else:
                            res = i
                    continue

        return res
