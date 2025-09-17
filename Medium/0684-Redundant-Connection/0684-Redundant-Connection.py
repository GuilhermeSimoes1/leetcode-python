class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = {}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return False
            parent[ry] = rx
            return True

        ultimo = []
        for u, v in edges:
            if u not in parent: parent[u] = u
            if v not in parent: parent[v] = v
            if not union(u, v):
                ultimo = [u, v]
        return ultimo
