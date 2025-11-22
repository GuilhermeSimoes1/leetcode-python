# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        def bst(root, contador):

            if root is None:
                return

            bst(root.left, contador)

            contador[root.val] = contador.get(root.val, 0) + 1

            bst(root.right, contador)

        contador = {}

        bst(root, contador)

        if contador:
            maxValue = max(contador.values())
        else:
            return [0]

        finalList = []

        for val, count in contador.items():

            if count == maxValue:
                finalList.append(val)

        return finalList