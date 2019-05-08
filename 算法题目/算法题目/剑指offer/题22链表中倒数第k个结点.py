# Author guo
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if not head or not k:
            return

        A = head
        B = None

        for i in range(k - 1):#循环次数
            if A.next != None:#可能为空
                A = A.next
            else:
                return

        B = head

        while A.next != None:
            A = A.next
            B = B.next

        return B