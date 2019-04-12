#Author guo
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        if root==None:
            return True
        return self.isSymmetrics(root.left,root.right)

    def isSymmetrics(self,t1,t2):
        if t1==None and t2==None:
            return True
        if t1==None or t2==None:
            return False
        if t1.val!=t2.val:
            return False
        return self.isSymmetrics(t1.left,t2.left) and self.isSymmetrics(t1.right,t2.right)
