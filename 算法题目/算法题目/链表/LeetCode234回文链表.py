#Author guo
# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def isPalindrome(self, head):
        #切成两半，后半段反转，比较两半是否相等
        if head==None or head.next==None:
            return True
        slow=head
        fast=head.next
        while (fast!=None and fast.next!=None):
            slow=slow.next
            fast=fast.next.next
        if fast!=None:
            slow=slow.next
        self.cut(head,slow)
        return self.isEqual(head,self.reverse(slow))

    def cut(self,head,cutNode):
        while head.next!=cutNode:
            head=head.next
        head.next=None

    def reverse(self,head):
        newhead=None
        while(head!=None):
            nextnode=head.next
            head.next=newhead
            newhead=head
            head=nextnode

        return newhead

    def isEqual(self,l1,l2):
        while l1!=None and l2!=None:
            if l1.val !=l2.val:
                return False
            l1=l1.next
            l2=l2.next
        return True