class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        finalArray = []

        for i in range(numRows):

            row = [1] * (i + 1)

            for y in range(1, i):
                row[y] = finalArray[i - 1][y - 1] + finalArray[i - 1][y]

            finalArray.append(row)

        return finalArray


