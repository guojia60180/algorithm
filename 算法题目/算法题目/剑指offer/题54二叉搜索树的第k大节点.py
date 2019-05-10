#Author guo
# -*- coding:utf-8 -*-
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


class Solution:
    # 返回对应节点TreeNode
    def __init__(self):
        self.res = []

    def KthNode(self, pRoot, k):
        # write code here
        if k == 0 or pRoot == None:
            return
        self.order(pRoot)
        if k > len(self.res):
            return
        return self.res[k - 1]

    def order(self, pRoot):
        if pRoot.left:
            self.order(pRoot.left)
        self.res.append(pRoot)

        if pRoot.right:
            self.order(pRoot.right)

