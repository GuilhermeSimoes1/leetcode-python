class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:

        m, n = len(mat), len(mat[0])

        if m * n != r * c:
            return mat

        normalList = []
        subList = []
        finalList = []
        value = 0

        for linha in mat:
            for elemento in linha:
                normalList.append(elemento)

        for i in range(r):

            subList = []

            while len(subList) < c:
                subList.append(normalList[value])
                value += 1

            finalList.append(subList)

        return finalList