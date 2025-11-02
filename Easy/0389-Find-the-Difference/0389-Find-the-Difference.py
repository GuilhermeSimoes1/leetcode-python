class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        Slist = list(s)

        for x in t:
            if x in Slist:
                Slist.remove(x)
                continue
            else:
                return x