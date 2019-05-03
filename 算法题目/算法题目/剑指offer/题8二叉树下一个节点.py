#Author guo
# -*- coding:utf-8 -*-
class TreeLinkNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
         self.next = None
pNode=TreeLinkNode()


class Solution:
    def GetNext(self, pNode):
        # write code here

        if not pNode:
            return None
        pNext = None
        if pNode.right != None:
            pRight = pNode.right
            while pRight.left != None:
                pRight = pRight.left
            pNext = pRight  # 下一个节点

        elif pNode.next != None:  # 父节点不为空
            pCur = pNode
            pPare = pCur.next

            while pPare != None and pCur == pPare.right:
                pCur = pPare
                pPare = pCur.next  # 再往上找，停止条件父节点不为空 且节点是父节点的右节点
            pNext = pPare

        return pNext

class Solution2:
    def GetNext(self,pNode):
        if pNode==None:
            return None

        pNext=None
        #如果输入节点有右子树，下一个节点是右子树的左节点
        if pNode.right:
            pNode=pNode.right
            while pNode.left!=None:
                pNode=pNode.left

            pNext=pNode

        else:
            #如果当前节点有父节点且是父节点左节点，下一个节点是父节点
            if pNode.next and pNode.next.left==pNode:
                pNext=pNode.next

            #如果当前节点有父节点，节点是父节点的右节点，向上遍历
            elif pNode.next and pNode.next.right==pNode:
                pPar=pNode.next
                pNode=pPar
                while pNode.next and pNode.next.right==pNode:
                    pNode=pNode.next

                #遍历终止时当前节点有父节点，说明当前节点是父节点的左子节点，输入节点的下一个节点是当前节点的父节点
                #当前节点没有父节点，说明当前节点位于根结点的右子树，没有下一个节点

                if pNode.next:
                    pNext=pNode.next

        return pNext