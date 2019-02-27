#Author guo
# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        dummy=jump=ListNode(0)
        dummy.next=head
        l=r=head

        while True:
            count=0
            while r and count<k:
                r=r.next
                count=count+1
            if count==k:
                pre,cur=r,l
                for i in range(k):
                    cur.next,cur,pre=pre,cur.next,cur
                jump.next,jump,l=pre,l,r
            else:
                return dummy.next

