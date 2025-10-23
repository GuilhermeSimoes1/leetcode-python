# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        def tree(node, s, final):

            if not node:
                return

            s.append(str(node.val))

            if node.left is None and node.right is None:

                final.append("->".join(s))

            else:
                tree(node.left, s, final)
                tree(node.right, s, final)

            s.pop()

        final = []
        tree(root, [], final)
        return final