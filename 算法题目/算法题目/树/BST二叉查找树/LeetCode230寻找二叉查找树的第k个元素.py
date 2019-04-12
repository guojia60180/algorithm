#Author guo
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    #写计数器，中序遍历，搜索树满足中序遍历有序，找到第k个
    def kthSmallest(self, root, k):
        self.cnt=0
        self.inorder(root,k)
        return self.val


    def inorder(self,node,k):
        if node==None:
            return
        self.inorder(node.left,k)
        self.cnt+=1
        if self.cnt==k:
            self.val=node.val
            return

        self.inorder(node.right,k)

    #递归

    def kthSmallest1(self, root, k):
        leftCnt=self.count(root.left)
        if leftCnt==k-1:
            return root.val
        if leftCnt>k-1:
            return self.kthSmallest1(root.left,k)
        return self.kthSmallest1(root.right,k-leftCnt-1)
    def count(self,node):
        if node==None:
            return 0
        return 1+self.count(node.left)+self.count(node.right)