class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        lista1 = [int(x) for x in num1]
        lista2 = [int(x) for x in num2]
        listaFinal = []

        while len(lista1) < len(lista2):
            lista1.insert(0, 0)
        while len(lista2) < len(lista1):
            lista2.insert(0, 0)

        bit = 0

        for i in range(len(lista1) - 1, -1, -1):
            res = lista1[i] + lista2[i] + bit

            if res >= 10:
                bit = 1
                res -= 10
            else:
                bit = 0

            listaFinal.append(res)

        if bit:
            listaFinal.append(bit)

        listaFinal.reverse()
        return ''.join(str(x) for x in listaFinal)
