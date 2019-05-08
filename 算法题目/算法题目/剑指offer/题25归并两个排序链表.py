#Author guo
# -*- coding:utf-8 -*-
class ListNode:
     def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if pHead1==None:
            return pHead2
        if pHead2==None:
            return pHead1

        pHead=None

        if(pHead1.val<pHead2.val):
            pHead=pHead1
            pHead.next=self.Merge(pHead1.next,pHead2)

        if(pHead1.val>=pHead2.val):
            pHead=pHead2
            pHead.next=self.Merge(pHead1,pHead2.next)

        return pHead