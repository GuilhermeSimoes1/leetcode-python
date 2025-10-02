class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:

        colunas = []
        count = 0

        for i in range(len(grid)):

            coluna = []

            for y in range(len(grid)):
                coluna.append(grid[y][i])
            colunas.append(coluna)

        for row in grid:
            for coluna in colunas:
                if row == coluna:
                    count += 1
        return count






