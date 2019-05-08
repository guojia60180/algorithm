#Author guo
# -*- coding:utf-8 -*-
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        reservedHead=None
        pNode=pHead
        pPre=None

        while pNode!=None:
            pNext=pNode.next

            if pNext==None:
                reservedHead=pNode

            pNode.next=pPre
            pPre=pNode
            pNode=pNext#进入下一个结点

        return reservedHead