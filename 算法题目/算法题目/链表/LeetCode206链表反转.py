#Author guo
# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None or head.next==None:
            return head

        l=head.next
        newhead=self.reverseList(l)
        l.next=head
        head.next=None
        return newhead
    #递归完成
#头插法

    def reverseList2(self,head):
        newhead=ListNode(-1)
        while head!=None:
            l=head.next
            head.next=newhead.next
            newhead.next=head
            head=l
        return newhead.next