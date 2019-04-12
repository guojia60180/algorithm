#Author guo
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        return self.toBST(nums,0,len(nums)-1)

    def toBST(self,nums,sidx,eidx):
        if sidx>eidx:
            return None
        midx=(sidx+eidx)//2
        root=nums[midx]
        root.left=self.toBST(nums,sidx,midx-1)
        root.right=self.toBST(nums,midx+1,eidx)
        return root
