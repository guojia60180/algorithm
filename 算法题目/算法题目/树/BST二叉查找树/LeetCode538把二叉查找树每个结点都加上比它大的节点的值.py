#Author guo
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root):
        self.sum=0
        self.traver(root)
        return root

#先遍历右子树，因为是按照顺序递增的，所以右子树最右不会变化
    def traver(self,node):
        if node==None:
            return
        self.traver(node.right)
        self.sum+=node.val
        node.val=self.sum
        self.traver(node.left)
#右中左进行中序遍历，完成相加的过程