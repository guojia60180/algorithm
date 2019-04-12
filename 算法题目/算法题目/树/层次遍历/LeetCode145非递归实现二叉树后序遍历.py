#Author guo
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root):
        ret = []
        stack = []
        stack.append(root)
        while stack:
            node = stack.pop()
            if node == None:
                continue

            ret.append(node.val)
            stack.append(node.left)
            stack.append(node.right)

        ret = reversed(ret)
        return ret