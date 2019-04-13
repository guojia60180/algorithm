#Author guo
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
class Solution:
    def averageOfLevels(self, root):
        q=collections.deque()
        res=[]
        q.append(root)
        while q:
            size=len(q)
            row=[]
            for x in range(size):
                node=q.popleft()
                if node==None:
                    continue
                row.append(node.val)
                q.append(node.left)
                q.append(node.right)
            if row:
                res.append(sum(row)//float(len(row)))
        return res
