# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def sumNodes(node, summ, target):

            if node is None:
                return False

            summ += node.val

            if node.right is None and node.left is None:
                return summ == target

            return sumNodes(node.right, summ, target) or sumNodes(node.left, summ, target)

        curr = root
        return sumNodes(curr, 0, targetSum)
