class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        dic = {}

        s = s.split()

        if len(pattern) != len(s):
            return False

        for x, y in zip(pattern, s):
            if x not in dic and y not in dic.values():
                dic[x] = y

            elif x in dic:
                if dic[x] != y:
                    return False
            else:
                return False

        return True



