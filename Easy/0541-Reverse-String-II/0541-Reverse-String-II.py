class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        count = 1

        lista = list(s)

        for i in range(0, len(s), 2 * k):
            lista[i:i + k] = lista[i:i + k][::-1]

        return "".join(lista)







