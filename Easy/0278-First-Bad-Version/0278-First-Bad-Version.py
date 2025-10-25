# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:

        inicio = 1
        fim = n

        while inicio < fim:

            meio = (inicio + fim) // 2

            res = isBadVersion(meio)

            if res == False:
                inicio = meio + 1
            else:
                fim = meio

        return fim


