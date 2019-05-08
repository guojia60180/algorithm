#Author guo
# -*- coding:utf-8 -*-
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        '''
        1.交换根结点的左右子树
        2.交换一个节点的左右子节点
        3.交换另一个结点的左右子节点
        '''
        if root==None:
            return None
        if not root.left and not root.right:
            return root

        root.left,root.right=root.right,root.left

        self.Mirror(root.left)
        self.Mirror(root.right)

    def Mirror2(self,root):
        if root==None:
            return
        stackNode=[]
        stackNode.append(root)
        while len(stackNode)>0:
            nodeNum=len(stackNode)-1
            tree=stackNode[nodeNum]
            stackNode.pop()
            nodeNum-=1
            if tree.left!=None or tree.right!=None:
                tree.left,tree.right=tree.right,tree.left
            if tree.left:
                stackNode.append(tree.left)
                nodeNum+=1
            if tree.right:
                stackNode.append(tree.right)
                nodeNum+=1

    def Mirrornorecursion(self,root):
        if root==None:
            return
        nodeQue=[root]
        while len(nodeQue)>0:
            curlevel,count=len(nodeQue),0
            while count<curlevel:
                count+=1
                proot=nodeQue.pop(0)
                proot.left,proot.right=proot.right,proot.left
                if proot.left:
                    nodeQue.append(proot.left)
                if proot.right:
                    nodeQue.append(proot.right)

pNode1 = TreeNode(8)
pNode2 = TreeNode(6)
pNode3 = TreeNode(10)
pNode4 = TreeNode(5)
pNode5 = TreeNode(7)
pNode6 = TreeNode(9)
pNode7 = TreeNode(11)

pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode2.right = pNode5
pNode3.left = pNode6
pNode3.right = pNode7

S = Solution()
S.Mirror(pNode1)
print(pNode1.right.left.val)