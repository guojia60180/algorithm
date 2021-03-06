#Author guo
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return None
        l=len(lists)
        if l==1:
            return lists[0]
        mid=l//2
        return self.mergeTwoLists(self.mergeKLists(lists[:mid]),self.mergeKLists(lists[mid:]))
#利用二分法，递归回另一个参数，分成两个部分，知道是两个值为止

    def mergeTwoLists(self, l1, l2) :

             cur=ListNode(0)
             dummy=cur
             while l1 and l2:
                 if l1.val>l2.val:
                     cur.next=l2
                     l2=l2.next
                     cur=cur.next
                 else:
                     cur.next=l1
                     l1=l1.next
                     cur=cur.next
             cur.next= l1 or l2
             return dummy.next#迭代实现