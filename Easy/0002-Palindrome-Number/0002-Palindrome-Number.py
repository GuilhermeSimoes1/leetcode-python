class Solution:
    def isPalindrome(self, x: int) -> bool:

        i = 0
        lista = []
        for element in str(x):
            lista.insert(i, element)
            i += 1

        y = -1
        z = 0
        lista2 = []
        for element2 in lista:
            numInv = lista[y]
            lista2.insert(z, numInv)
            y -= 1
            z += 1

        if lista == lista2:
            return True
        else:
            return False

