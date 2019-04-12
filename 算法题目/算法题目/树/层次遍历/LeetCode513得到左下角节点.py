#Author guo
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
class Solution:
    def findBottomLeftValue(self, root):
        q=collections.deque()
        q.append(root)
        while q:
            root=q.popleft()
            if root.right!=None:
                q.append(root.right)
            if root.left!=None:
                q.append(root.left)

        return root.val
