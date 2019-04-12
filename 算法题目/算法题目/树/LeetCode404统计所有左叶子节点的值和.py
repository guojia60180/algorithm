#Author guo
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root):
        if root==None:
            return 0
        if self.isLeaf(root.left):
            return root.left.val+self.sumOfLeftLeaves(root.right)

        return self.sumOfLeftLeaves(root.left)+self.sumOfLeftLeaves(root.right)


    def isLeaf(self,node):
        if node==None:
            return False
        return  node.left==None and node.right==None
