#Author guo
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head):
        if head == None or head.next == None:
            return head
        head.next = self.deleteDuplicates(head.next)

        return head.next if head.val == head.next.val else head