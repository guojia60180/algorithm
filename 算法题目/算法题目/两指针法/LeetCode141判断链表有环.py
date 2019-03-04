#Author guo
# Definition for singly-linked list.
#构建两个指针，如果一个一次前进一格，一个一次前进两个，当他们之间会相等时，认为链表中有环
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        pre=head
        cur=head
        while cur and pre and cur.next:#当都存在时
            pre=pre.next

            cur=cur.next.next
            if cur==pre:
                return True
        return False
