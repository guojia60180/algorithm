#Author guo
# -*- coding:utf-8 -*-
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

#通过遍历序列是否相同，写出两个遍历序列，比较是否相同
class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        return self.isSymm(pRoot,pRoot)

    def isSymm(self,root1,root2):
        if root1==None and root2==None:
            return True
        if root1==None or root2==None:
            return False

        root1list=self.front(root1,[])
        root2list=self.back(root2,[])
        print(root1list)
        print(root2list)
        return root1list==root2list


    def front(self,root,x=[]):

        if root==None:
            return x.append(99999)
        x.append(root.val)
        #print(x)
        self.front(root.left,x)
        self.front(root.right,x)
        return x

    def back(self,root,y=[]):
        if root==None:
            return y.append(99999)
        y.append(root.val)
        #print(y)
        self.back(root.right,y)
        self.back(root.left,y)
        return y


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
result = S.isSymmetrical(pNode1)
print(result)