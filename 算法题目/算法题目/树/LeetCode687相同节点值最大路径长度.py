#Author guo
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root):
        #把自己看成为一个根节点
        #最长路径要么是左子树的最长路径数
        #右子树的最长路径数
#左右子树的路径数相加
        self.path=0
        self.dfs(root)
        return self.path

    def dfs(self,root):
        if root==None:
            return 0
        l=self.dfs(root.left)
        r=self.dfs(root.right)
        leftpath=l+1 if root.left!=None and root.left.val==root.val else 0
        rightpath=r+1 if root.right!=None and root.right.val==root.val else 0
        self.path=max(self.path,leftpath+rightpath)
        return max(leftpath,rightpath)