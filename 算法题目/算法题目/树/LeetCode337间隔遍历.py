#Author guo
#不能同时偷两行树的结构

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root):
        if root==None:
            return 0
        self.value=root.val
        if root.left!=None:
            self.value+=self.rob(root.left.left)+self.rob(root.left.right)
        if root.right!=None:
            self.value++self.rob(root.right.left)+self.rob(root.right.right)

        self.total_value=self.rob(root.left)+self.rob(root.right)
        return max(self.value,self.total_value)