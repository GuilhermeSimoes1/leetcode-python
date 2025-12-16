class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:

        mat = [[0] * n for _ in range(m)]

        for op in ops:

            for i in range(op[0]):

                for j in range(op[1]):

                    mat[i][j] += 1

        maior = 0
        count = 0

        for i in range(m):

            for j in range(n):

                if mat[i][j] > maior:

                    maior = mat[i][j]

                    count = 1

                elif mat[i][j] == maior:

                    count += 1

        return count
