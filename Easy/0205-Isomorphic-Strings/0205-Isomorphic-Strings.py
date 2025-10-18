class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        dicS = {}
        dicT = {}

        for x, y in zip(s, t):

            if x not in dicS and y not in dicT:
                dicS[x] = y
                dicT[y] = x

            if x in dicS or y in dicT:
                if dicS.get(x) != y or dicT.get(y) != x:
                    return False
        return True