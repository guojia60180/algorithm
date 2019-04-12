#Author guo
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        #平衡左右子树高度差小于等于1
        if root==None:
            return True
        l_depth=self.depth(root.left)
        r_depth=self.depth(root.right)

        if abs(l_depth-r_depth)<=1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False

    def depth(self,root):
        if not root:
            return 0


        return 1+max(self.depth(root.right),self.depth(root.left))
