class Solution:
    def thirdMax(self, nums: List[int]) -> int:

        lista = list(set(nums))

        lista.sort(reverse=True)

        print(lista)

        if len(lista) < 3:
            maxx = 0

            for x in lista:

                if x > maxx:
                    maxx = x

            return maxx

        else:

            return lista[2]








