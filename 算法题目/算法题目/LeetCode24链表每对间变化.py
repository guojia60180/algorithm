#Author guo

class ListNode:
     def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        if not head or not head.next:
            return head

        cur=dummy=ListNode(-1)
        dummy.next=head

        while cur.next and cur.next.next:
            a,b=cur.next,cur.next.next

            a.next,b.next,cur.next=b.next,a,b

            cur=cur.next.next

        return dummy.next







