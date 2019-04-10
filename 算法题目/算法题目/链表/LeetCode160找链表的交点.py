#Author guo
#找出两个链表的交点
#A的长度a+c B的长度b+c c为公共部分长度
#a+c+b=b+c+a

#当访问A链表指针访问到链表尾部时，令从B链表头部访问链表B
#控制访问AB两个链表指针能同时访问到交点

#Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        
        """
        l1=headA
        l2=headB
        while l1!=l2:
            l1=headB if l1==None else l1.next
            l2=headA if l2==None else l2.next

        return l1

'''
如果只判断是否存在交点
1.把第一个链表结尾连接到第二个链表的开头，看第二个链表是否存在环

2.直接比较两个链表的最后一个节点是否相同
'''