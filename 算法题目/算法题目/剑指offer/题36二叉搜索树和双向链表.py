#Author guo
# -*- coding:utf-8 -*-
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        if pRootOfTree==None:
            return None
        if not pRootOfTree.left and not pRootOfTree.right:
            return pRootOfTree

        #处理左子树 左边最右节点与根结点相连

        self.Convert(pRootOfTree.left)
        left=pRootOfTree.left
        if left:
            while left.right:
                left=left.right
            pRootOfTree.left=left
            left.right=pRootOfTree
        #处理右子树，最左与根结点相连

        self.Convert(pRootOfTree.right)
        right=pRootOfTree.right
        if right:
            while right.left:
                right=right.left
            pRootOfTree.right=right
            right.left=pRootOfTree


        while pRootOfTree.left:
            pRootOfTree=pRootOfTree.left
        return pRootOfTree

