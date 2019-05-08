#Author guo
'''
第一种：
复制分为两部分
第一步复制原始链表上每个结点N创建N'，创建的节点用Next指针连接
同时把<N,N'>的配对信息放到一个哈希表
第二步设置复制链表每个结点
第二种：
第一步直接在每个结点后创建对应的N'
第二步设置复制出的结点的随机指针
第三步长链表拆分成两个链表，奇数位置连接起来就是原始链表，偶数位置连起来就是复制链表

'''
# -*- coding:utf-8 -*-
class RandomListNode:
     def __init__(self, x):
         self.label = x
         self.next = None
         self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if pHead==None:
            return None
        self.CloneNodes(pHead)
        self.ConnectRandomNodes(pHead)
        return self.ReconnectNodes(pHead)

    #复制原始链表的每个结点，将复制的结点连接在原始结点后面
    def CloneNodes(self,pHead):
        pNode=pHead
        while pNode:
            pCloned=RandomListNode(0)
            pCloned.label=pNode.label
            pCloned.next=pNode.next


            pNode.next=pCloned
            pNode=pCloned.next

    #将复制后的链表复制结点的random指针链接到被复制结点random指针的后一个节点
    def ConnectRandomNodes(self,pHead):
        pNode=pHead
        while pNode:
            pCloned=pNode.next
            if pNode.random!=None:
                pCloned.random=pNode.random.next
            pNode=pCloned.next

    #拆分链表，原始链表结点组成新的链表，复制结点组成复制后的链表
    def ReconnectNodes(self,pHead):
        pNode=pHead
        pClonedHead=pClonedNode=pNode.next
        pNode.next=pClonedHead.next
        pNode=pNode.next

        while pNode:
            pClonedNode.next=pNode.next
            pClonedNode=pClonedNode.next
            pNode.next=pClonedNode.next
            pNode=pNode.next

        return pClonedHead