# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def pathFinder(self, root, path, n):

        if root is None:
            return False

        path.append(root)

        if root == n or self.pathFinder(root.left, path, n) or self.pathFinder(root.right, path, n):
            return True

        path.pop()
        return False

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        path1 = []
        path2 = []

        self.pathFinder(root, path1, p)

        self.pathFinder(root, path2, q)


        value = None
        i = 0
        while i < len(path1) and i < len(path2):
            if path1[i] == path2[i]:
                value = path1[i]
            i += 1
        print(value)
        return value