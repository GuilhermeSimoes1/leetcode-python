# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        if root is None:
            return []

        def preOrder(node, final):

            if node is None:
                return

            final.append(node.val)

            preOrder(node.left, final)

            preOrder(node.right, final)

            return final

        finalResult = []
        curr = root
        return preOrder(curr, finalResult)
