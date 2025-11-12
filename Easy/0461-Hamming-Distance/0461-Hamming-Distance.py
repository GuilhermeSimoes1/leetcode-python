class Solution:
    def hammingDistance(self, x: int, y: int) -> int:

        binarioX = bin(x)
        binarioY = bin(y)

        binarioX = binarioX[2:]
        binarioY = binarioY[2:]

        if len(binarioX) > len(binarioY):

            listaBinY = list(binarioY)

            for _ in range(len(binarioX) - len(binarioY)):
                listaBinY.insert(0, "0")

            binarioY = "".join(listaBinY)

        elif len(binarioX) < len(binarioY):

            listaBinX = list(binarioX)

            for _ in range(len(binarioY) - len(binarioX)):
                listaBinX.insert(0, "0")

            binarioX = "".join(listaBinX)

        print(binarioX)
        print(binarioY)

        count = 0
        for x, y in zip(binarioX, binarioY):

            if x != y:
                count += 1

        return count

