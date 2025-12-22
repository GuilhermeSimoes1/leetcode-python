class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:

        m, n = len(img), len(img[0])

        final = [[0] * n for _ in range(m)]

        for i in range(m):

            for j in range(n):

                soma = 0
                count = 0

                for delta_i in [-1, 0, 1]:

                    for delta_j in [-1, 0, 1]:

                        ni = i + delta_i

                        nj = j + delta_j

                        if 0 <= ni < m and 0 <= nj < n:
                            soma += img[ni][nj]

                            count += 1

                final[i][j] = soma // count

        return final
