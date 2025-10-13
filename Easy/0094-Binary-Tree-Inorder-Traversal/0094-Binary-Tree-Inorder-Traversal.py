# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        def inOrder(node, res):

            if node is None:
                return None

            inOrder(node.left, res)

            res.append(node.val)

            inOrder(node.right, res)

            return res

        if root is None:
            return []
        else:
            curr = root
            res = []

            return inOrder(curr, res)




