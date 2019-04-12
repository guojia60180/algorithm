#Author guo
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s, t):
        if s==None:
            return False
        return self.issubtreeWithRoot(s,t) or self.isSubtree(s.left,t) or self.isSubtree(s.right,t)

    def issubtreeWithRoot(self,s,t):
        if t==None and s==None:
            return True
        if t==None or s==None:
            return False
        if t.val!=s.val:
            return False
        return self.issubtreeWithRoot(s.left,t.left) and self.issubtreeWithRoot(s.right,t.right)

