#Author guo
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head):
        nums=[]
        while head:
            nums.append(head.val)
            head=head.next
        return self.toTree(nums)

    def toTree(self,nums):
        if not nums:
            return None
        l=len(nums)
        mid=l//2
        root=TreeNode(nums[mid])
        root.left=self.toTree(nums[:mid])
        root.right=self.toTree(nums[mid+1:])
        return root