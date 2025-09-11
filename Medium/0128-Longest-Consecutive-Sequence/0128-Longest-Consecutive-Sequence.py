class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        listaNoDuplicates = set(nums)
        listaOrdenada = sorted(listaNoDuplicates)
        value = 0
        aux = 0

        print(listaOrdenada)

        for i in range(0, len(listaOrdenada)):

            if i == 0:
                aux += 1
                continue

            if i + 1 < len(listaOrdenada) and listaOrdenada[i] == listaOrdenada[i - 1] + 1 and listaOrdenada[i] == \
                    listaOrdenada[i + 1] - 1:
                aux += 1

            if i + 1 < len(listaOrdenada) and listaOrdenada[i] == listaOrdenada[i - 1] + 1 and listaOrdenada[i] != \
                    listaOrdenada[i + 1] - 1:
                aux += 1
                if value < aux:
                    value = aux
                    aux = 0
                else:
                    aux = 0

            if i + 1 < len(listaOrdenada) and listaOrdenada[i] != listaOrdenada[i - 1] + 1 and listaOrdenada[i] == \
                    listaOrdenada[i + 1] - 1 and aux >= 0:
                aux = 0
                aux += 1

            if i + 1 == len(listaOrdenada) and listaOrdenada[i] == listaOrdenada[i - 1] + 1:
                aux += 1

        if value < aux:
            value = aux

        return value




