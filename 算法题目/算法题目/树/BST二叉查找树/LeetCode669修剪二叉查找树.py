#Author guo
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#剔除非L-R范围内的值
class Solution:
    def trimBST(self, root, L, R):
        if root==None:
            return None
        if root.val>R:
            return self.trimBST(root.left,L,R)#剔除过程，返回到函数，去掉当前节点，直接指向root.lkeft
        if root.val<L:
            return self.trimBST(root.right,L,R)
        root.left=self.trimBST(root.left,L,R)#遍历过程
        root.right=self.trimBST(root.right,L,R)#遍历过程
        return root
