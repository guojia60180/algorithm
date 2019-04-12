#Author guo
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        #包含所有的根节点
        if root==None:
            return 0
        self.res=self.pathwithstart(root,sum)+self.pathwithstart(root.left,sum)+self.pathwithstart(root.right,sum)
        return self.res
    def pathwithstart(self,root,sum):
        if root==None:
            return 0
        self.res=0
        if root.val==sum:
            self.res+=1
        self.res+=self.pathwithstart(root.left,sum-root.val)+self.pathwithstart(root.right,sum-root.val)
        return self.res
