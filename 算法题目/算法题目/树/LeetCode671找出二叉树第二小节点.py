#Author guo
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root):
        if root==None:
            return -1
        if root.left==None and root.right==None:
            return -1

        leftVal=root.left.val
        rightVal=root.right.val
        if leftVal==root.val:
            leftVal=self.findSecondMinimumValue(root.left)
        if rightVal==root.val:
            rightVal=self.findSecondMinimumValue(root.right)
        if leftVal!=-1 and rightVal!=-1:
            return min(leftVal,rightVal)
        if leftVal!=-1:
            return leftVal
        return rightVal
