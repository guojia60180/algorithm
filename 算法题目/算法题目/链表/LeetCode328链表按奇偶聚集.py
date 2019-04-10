#Author guo
# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def oddEvenList(self, head):
        if head==None:
            return head
        odd=head
        even=head.next
        evenhead=even

        while even !=None and even.next!=None:
            odd.next=odd.next.next
            odd=odd.next
            even.next=even.next.next
            even=even.next

        odd.next=evenhead
        return head