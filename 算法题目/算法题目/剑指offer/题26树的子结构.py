#Author guo
# -*- coding:utf-8 -*-
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        res=False

        if pRoot1!=None and pRoot2!=None:
            if pRoot1.val==pRoot2.val:
                res=self.Tree1containsTree2(pRoot1,pRoot2)

            if not res:
                res=self.HasSubtree(pRoot1.left,pRoot2)

            if not res:
                res=self.HasSubtree(pRoot1.right,pRoot2)

        return res

    def Tree1containsTree2(self,pRoot1,pRoot2):
        if pRoot2==None:
            return True
        if pRoot1==None:
            return False

        if pRoot1.val!=pRoot2.val:
            return False

        return self.Tree1containsTree2(pRoot1.left,pRoot2.left) and self.Tree1containsTree2(pRoot1.right,pRoot2.right)

pRoot1 = TreeNode(8)
pRoot2 = TreeNode(8)
pRoot3 = TreeNode(7)
pRoot4 = TreeNode(9)
pRoot5 = TreeNode(2)
pRoot6 = TreeNode(4)
pRoot7 = TreeNode(7)
pRoot1.left = pRoot2
pRoot1.right = pRoot3
pRoot2.left = pRoot4
pRoot2.right = pRoot5
pRoot5.left = pRoot6
pRoot5.right = pRoot7

pRoot8 = TreeNode(8)
pRoot9 = TreeNode(9)
pRoot10 = TreeNode(2)
pRoot8.left = pRoot9
pRoot8.right = pRoot10

S = Solution()
print(S.HasSubtree(pRoot1, pRoot8))