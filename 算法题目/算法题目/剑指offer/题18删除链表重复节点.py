#Author guo
'''

删除结点的时候，常规做法是直接从头结点遍历到目标结点，然后进行删除

现在优化方法
把下一个节点内容不知道需要删除的节点上覆盖原有的内容，把下一个节点删除
删除结点i，先把下一个节点j的内容复制到i，然后把i的指针指向结点j的下一个节点

有一个关键的问题是，判断该节点是否在链表中
'''
# -*- coding:utf-8 -*-
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None
     def __del__(self):
         self.val=None
         self.next=None
#删除重复的节点
#在一个排序的列表中，存在重复的节点，删除重复节点
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if pHead==None:
            return
        preHead=None
        pNode=pHead
        while pNode!=None:
            flag=False
            NextNode=pNode.next

            if NextNode!=None and NextNode.val==pNode.val:
                flag=True
            if flag==False:
                preHead=pNode
                pNode=pNode.next
            else:
                nodeVal=pNode.val
                pdelete=pNode
                while pdelete!=None and pdelete.val==nodeVal:
                    pdelete=pdelete.next#循环删除

                if preHead==None:
                    pHead=pdelete
                    pNode=pdelete
                    continue

                else:
                    preHead.next=pdelete
                pNode=preHead

        return pHead