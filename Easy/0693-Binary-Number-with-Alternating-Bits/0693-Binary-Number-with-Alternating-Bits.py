class Solution:
    def hasAlternatingBits(self, n: int) -> bool:

        numBin = bin(n)

        print(numBin[2:])

        prev = ""

        for x in numBin:

            if prev == x:
                return False
            prev = x

        return True