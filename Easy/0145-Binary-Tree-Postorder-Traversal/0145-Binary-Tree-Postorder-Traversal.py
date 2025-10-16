# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        if root is None:
            return []

        def postOrder(node, final):

            if node is None:
                return

            postOrder(node.left, final)

            postOrder(node.right, final)

            final.append(node.val)

            return final

        finalResult = []
        curr = root
        return postOrder(curr, finalResult)