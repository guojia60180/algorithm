#Author guo
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        pre = head
        length = 0
        while (pre):
            length = length + 1
            pre = pre.next

        if length == n:
            return head.next

        else:
            cur = head

            for i in range(length - n - 1):
                cur = cur.next

            cur.next = cur.next.next

        return head