#Author guo
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root):
        #利用二叉查找树的中序遍历有序的性质，计算中序遍历
        #临近两个节点之差的绝对值，取最小值
        self.minDiff=int(float('inf'))
        self.preNode=None
        self.inOrder(root)
        return self.minDiff
    def inOrder(self,node):
        if node==None:
            return
        self.inOrder(node.left)
        if self.preNode!=None:
            self.minDiff=min(self.minDiff,node.val-self.preNode.val)
        self.preNode=node
        self.inOrder(node.right)