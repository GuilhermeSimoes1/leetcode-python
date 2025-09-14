# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def helper(node: Optional[TreeNode], fila: list):

            if not node:
                return
            fila.append(node.val)
            helper(node.right, fila)
            helper(node.left, fila)
            return fila

        filaFinal = helper(root, [])
        print(filaFinal)
        setted = set(filaFinal)
        sort = sorted(setted)
        print(sort)
        for i in range(0, k):
            value = sort[i]
        return value

