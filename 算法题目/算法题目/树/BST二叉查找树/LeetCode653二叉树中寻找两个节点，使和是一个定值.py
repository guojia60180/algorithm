#Author guo
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(self, root, k):
        #中序遍历得到有序数组后，双指针对数组进行查找
        #不能使用分别在左右子树处理，因为可能两个待求数分别在左右子树中
        self.nums=[]
        self.inorder(root,self.nums)
        i=0
        j=len(self.nums)-1
        while i<j:
            sum=self.nums[i]+self.nums[j]
            if sum==k:
                return True
            elif sum<k:
                i=i+1
            else:
                j=j-1
        return False


    def inorder(self,root,nums):
        if root==None:
            return
        self.inorder(root.left,nums)
        nums.append(root.val)
        self.inorder(root.right,nums)

    def inorder(self,root,nums):
        if root==None:
            return
        self.inorder(root.left,nums)
        self.nums.append(root.val)
        self.inorder(root.right,nums)
