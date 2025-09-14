# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if not preorder and not inorder:
            return
        node = TreeNode(preorder[0])

        left = []
        right = []

        indexNode = inorder.index(node.val)

        for i in range(0, indexNode):
            left.append(inorder[i])

        for y in range(indexNode + 1, len(inorder)):
            right.append(inorder[y])

        len_left = indexNode

        inorderListLeft = left
        preorderListLeft = preorder[1:len_left + 1]
        inorderListRight = right
        preorderListRight = preorder[len_left + 1:]
        node.left = self.buildTree(preorderListLeft, inorderListLeft)
        node.right = self.buildTree(preorderListRight, inorderListRight)
        return node




