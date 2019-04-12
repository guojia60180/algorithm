#Author guo
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root):
        ret=[]
        stack=[]
        stack.append(root)
        while stack:
            node=stack.pop()
            if node==None:
                continue#跳出当前循环剩余语句，继续进行下一次循环
            ret.append(node.val)
            stack.append(node.right)#先右再左，保证左子树先遍历
            stack.append(node.left)

        return ret