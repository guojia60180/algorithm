#Author guo
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#路径和定义为从根节点到叶子结点的值的和
class Solution:
    def hasPathSum(self, root, sum):
        if root==None:
            return False
        if root.left==None and root.right==None and root.val==sum:
            return True
        return self.hasPathSum(root.left,sum-root.val) or self.hasPathSum(root.right,sum-root.val)

