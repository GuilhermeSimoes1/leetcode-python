# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        lista = []

        def getNodes(root, lista):

            if root is None:
                return

            lista.append(root.val)

            getNodes(root.left, lista)

            getNodes(root.right, lista)

        getNodes(root, lista)

        lista.sort()

        if len(lista) > 1:

            minDiff = abs(lista[0] - lista[1])

            for i in range(2, len(lista)):
                minDiff = min(minDiff, abs(lista[i] - lista[i - 1]))

            return minDiff
        else:
            return lista[0]






