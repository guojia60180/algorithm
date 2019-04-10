#Author guo
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        if not head or not head.next:
            return head

        cur = dummy = ListNode(0)
        dummy.next = head
        cur = dummy

        while cur and cur.next:
            a, b = cur, cur.next

            a.next, b.next, cur = b.next, a, b  # 交换过程，画图

            cur = cur.next.next  # 往下进行两个结点

        return dummy
