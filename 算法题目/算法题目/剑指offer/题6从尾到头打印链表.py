#Author guo
# -*- coding:utf-8 -*-
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None


class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here

        if listNode == None:
            return []
        stack = []
        l = []
        head = listNode
        while head:
            stack.append(head.val)
            #l.insert(0, (stack.pop()))
            head = head.next
        while stack:
            l = l + [stack.pop()]
        return l
#逆序的方法有很多种，不进行演示