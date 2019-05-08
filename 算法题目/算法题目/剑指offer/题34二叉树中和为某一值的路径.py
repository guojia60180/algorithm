#Author guo
# -*- coding:utf-8 -*-
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return []
        if root.left==None and root.right==None:
            if expectNumber==root.val:
                return [[root.val]]
            else:
                return []

        stack=[]
        leftstack=self.pathSum(root.left,expectNumber-root.val)
        for i in leftstack:
            i.insert(0,root.val)
            stack.append(i)
        rightstack=self.pathSum(root.right,expectNumber-root.val)
        for i in rightstack:
            i.insert(0,root.val)
            stack.append(i)
        return stack




    def pathSum(self,root,expectednumber):
        if not  root:
            return []
        if root.left==None and root.right==None:
            if expectednumber==root.val:
                return [[root.val]]
            else:
                return []

        a=self.pathSum(root.left,expectednumber-root.val)+self.pathSum(root.right,expectednumber-root.val)
        return [[root.val]+i for i in a]

pNode1 = TreeNode(10)
pNode2 = TreeNode(5)
pNode3 = TreeNode(12)
pNode4 = TreeNode(4)
pNode5 = TreeNode(7)


pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode2.right = pNode5


S = Solution()
print(S.FindPath(pNode1, 22))
# 测试用例：[1,-2,-3,1,3,-2,null,-1]  -1
# 测试用例：[-2, None, -3] -5