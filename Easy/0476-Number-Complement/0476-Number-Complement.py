class Solution:
    def findComplement(self, num: int) -> int:

        numBin = bin(num)
        numBin = numBin[2:]
        numBin = list(numBin)

        for i in range(len(numBin)):
            if numBin[i] == "1":
                numBin[i] = "0"
            else:
                numBin[i] = "1"

        numBin = "".join(numBin)

        return int(numBin, 2)