# Author guo
# -*- coding:utf-8 -*-
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None
# 思路：1.判断是否有环 快慢指针
# 2.计数器计算环的长度
# 3.两个慢指针，一个从起点出发，一个从环的长度出发
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if not pHead:
            return None

        A = pHead
        B = pHead
        if pHead.next == None:
            return None
        A = pHead.next.next
        if not A:
            return None
        B = pHead.next
        if not B:
            return None
        count = 1
        while A:
            if A != B:
                A = A.next.next
                B = B.next
                count += 1
            else:
                break
        C = pHead
        D = None
        for i in range(count):
            if C.next != None:
                C = C.next

        D = pHead
        while C != D:
            C = C.next
            D = D.next

        return C
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node3

s = Solution()
print(s.EntryNodeOfLoop(node1).val)