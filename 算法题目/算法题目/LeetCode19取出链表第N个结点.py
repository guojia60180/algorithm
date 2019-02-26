#Author guo
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None
class Solution(object):
    def removeNthFromEnd(self,head,n):
        pre=head
        length=0
        while(pre):#如果存在pre指针，统计链表长度
            length=length+1
            pre=pre.next

        if length==n:#如果长度与n相等，去除第一个结点
            return  head.next
        else:
            cur=head
            for i in range(length-n-1):
                cur=cur.next#找到第n个结点

            cur.next=cur.next.next#去除那个结点
            return head