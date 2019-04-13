#Author guo
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        ret=[]
        if root==None:
            return  ret
        stack=[]
        cur=root
        while cur!=None or stack:
            while cur!=None:
                stack.append(cur)
                cur=cur.left

            node=stack.pop()
            ret.append(node.val)
            cur=node.right

        return ret
