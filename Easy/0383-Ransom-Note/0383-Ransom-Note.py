class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        res = []
        Listmagazine = []

        for i in magazine:
            Listmagazine.append(i)

        for x in ransomNote:
            if x in Listmagazine:
                res.append(x)
                Listmagazine.remove(x)

        if len(res) == len(ransomNote):
            return True
        else:
            return False