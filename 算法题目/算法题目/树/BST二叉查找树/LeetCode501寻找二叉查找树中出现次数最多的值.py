#Author guo
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
class Solution:
    def findMode(self, root):
      if root==None:
          return []
      self.count=collections.Counter()
      self.inorder(root)
      freq=max(self.count.values())
      res=[]
      for item,c in self.count.items():
          if c==freq:
              res.append(item)#利用标准库中的计数器计算哈希，建立字典
      return res

    def inorder(self,root):
        if root==None:
            return
        self.inorder(root.left)
        self.count[root.val]+=1
        self.inorder(root.right)
