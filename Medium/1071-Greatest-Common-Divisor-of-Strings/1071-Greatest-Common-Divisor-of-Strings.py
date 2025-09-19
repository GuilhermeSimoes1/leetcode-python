class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        n1, n2 = len(str1), len(str2)
        limite = min(n1, n2)

        for size in range(limite, 0, -1):
            if n1 % size == 0 and n2 % size == 0:
                candidato = str1[:size]
                if candidato * (n1 // size) == str1 and candidato * (n2 // size) == str2:
                    return candidato
        return ""





