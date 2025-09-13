# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        fila = deque([root])
        result = []

        while fila:

            nivel = []
            for _ in range(len(fila)):
                node = fila.popleft()
                nivel.append(node.val)
                if node.left:
                    fila.append(node.left)
                if node.right:
                    fila.append(node.right)
            result.append(nivel)

        return result
