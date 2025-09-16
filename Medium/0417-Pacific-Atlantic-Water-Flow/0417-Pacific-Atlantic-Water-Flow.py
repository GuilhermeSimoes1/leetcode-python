class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        rows, cols = len(heights), len(heights[0])
        if rows == 1 and cols == 1:
            return [[0, 0]]

        def bfs(starts):

            visited = set(starts)
            q = deque(starts)

            while q:
                r, c = q.popleft()
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc

                    if (
                            0 <= nr < rows and 0 <= nc < cols
                            and (nr, nc) not in visited
                            and heights[nr][nc] >= heights[r][c]
                    ):
                        visited.add((nr, nc))
                        q.append((nr, nc))
            return visited

        pacific = [(0, c) for c in range(cols)] + [(r, 0) for r in range(rows)]
        atlantic = [(rows - 1, c) for c in range(cols)] + [(r, cols - 1) for r in range(rows)]

        reach_pacific = bfs(pacific)
        reach_atlantic = bfs(atlantic)

        return [[r, c] for (r, c) in reach_pacific & reach_atlantic]

