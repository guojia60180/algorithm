#Author guo
# -*- coding:utf-8 -*-
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None


class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        len1 = 0
        len2 = 0
        pNode1 = pHead1
        pNode2 = pHead2
        while pNode1 != None:
            pNode1 = pNode1.next
            len1 += 1
        while pNode2 != None:
            pNode2 = pNode2.next
            len2 += 1

        if len1 > len2:
            p = len1 - len2
            while p > 0:
                pHead1 = pHead1.next
                p -= 1

        if len2 > len1:
            q = len2 - len1
            while q > 0:
                pHead2 = pHead2.next
                q -= 1

        while pHead1 != None and pHead2 != None and pHead1 != pHead2:
            pHead1 = pHead1.next
            pHead2 = pHead2.next

        return pHead1
