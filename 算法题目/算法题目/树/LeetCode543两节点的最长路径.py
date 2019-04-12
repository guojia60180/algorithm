#Author guo
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root):
        self.max=0
        self.depth(root)
        return self.max

    def depth(self,root):
        if root==None:
            return 0
        leftdepth=self.depth(root.left)
        rightdepth=self.depth(root.right)
        self.max=max(self.max,leftdepth+rightdepth)
        return max(leftdepth,rightdepth)+1