class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        dic1 = defaultdict(int)
        dic2 = defaultdict(int)
        lista1 = []
        lista2 = []

        if len(word1) != len(word2):
            return False

        if set(word1) != set(word2):
            return False

        for x in word1:
            key = x
            dic1[key] += 1

        for y in word2:
            key = y
            dic2[key] += 1

        for x in dic1:
            lista1.append(dic1[x])

        for x in dic2:
            lista2.append(dic2[x])

        if sorted(lista1) == sorted(lista2):
            return True
        else:
            return False


