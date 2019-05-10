#Author guo
# -*- coding:utf-8 -*-
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if pRoot == None:
            return 0
        n1 = self.TreeDepth(pRoot.left)
        n2 = self.TreeDepth(pRoot.right)

        return n1 + 1 if n1 > n2 else n2 + 1
    def __init__(self):
        self.flag=True
    def getDepth(self,pRoot):
        if pRoot==None:
            return 0
        left=1+self.getDepth(pRoot.left)
        right=1+self.getDepth(pRoot.right)

        if abs(left-right)>1:
            self.flag=False

        return left if left>right else right

    def IsBalanced(self,pRoot):
        self.getDepth(pRoot)
        return self.flag