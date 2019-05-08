#Author guo
# -*- coding:utf-8 -*-
import collections
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


import collections


class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    # 考虑使用一个队列，每次出队一个数，就把它的左右节点加入到这个队列
    def PrintFromTopToBottom(self, root):
        # write code here
        que = collections.deque()
        if root == None:
            return []

        que.append(root)
        # level=0
        # beprinted=1
        res = []
        while len(que) > 0:
            node = que.popleft()
            # print(node.val)
            res.append(node.val)

            if node.left:
                que.append(node.left)
                # level+=1
            if node.right:
                que.append(node.right)
        return res       # level+=1

            #que.popleft()
            # beprinted-=1

            # if beprinted==0:
            # print('\n')
            # beprinted=level
            # level=0


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
print(S.PrintFromTopToBottom(pNode1))