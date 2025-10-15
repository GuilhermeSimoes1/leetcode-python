class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        finalList = []

        for i in range(rowIndex + 1):

            row = [1] * (i + 1)

            for y in range(1, i):
                row[y] = finalList[i - 1][y - 1] + finalList[i - 1][y]

            finalList.append(row)

        return finalList[-1]