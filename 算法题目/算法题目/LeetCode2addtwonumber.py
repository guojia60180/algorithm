#Author guo
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0
        sum = ListNode(0)
        s = sum
        while l1 is not None or l2 is not None or carry:
            s.val = carry
            if l1:
                s.val += l1.val
                l1 = l1.next
            if l2:
                s.val += l2.val
                l2 = l2.next
            carry = s.val // 10
            s.val = s.val % 10
            if l1 or l2 or carry:
                s.next = ListNode(0)
                s = s.next
        return sum