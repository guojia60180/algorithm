#Author guo
'''
输入某二叉树的前序和中序遍历结果，重建二叉树
'''

'''
方法：
1.从前序遍历的第一个值是根结点
2.在中序遍历中找根结点，根结点之前的是左子树，根结点之后的是右子树
3.左子树的节点在前序遍历中能找到第一个值，根结点
.....循环下去构建树
'''

# -*- coding:utf-8 -*-
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not pre or not  tin:
            return None
        root=TreeNode(pre[0])
        i=tin.index(pre[0])
        root.left=self.reConstructBinaryTree(pre[1:i+1],tin[0:i])
        root.right=self.reConstructBinaryTree(pre[i+2:],tin[i+1:])
        return root

    #按层序遍历输出某层的值
    def PrintNodeAtLevel(self,treeNode, level):
        if not treeNode or level < 0:
            return 0
        if level == 0:
            print(treeNode.val)
            return 1
        self.PrintNodeAtLevel(treeNode.left, level-1)
        self.PrintNodeAtLevel(treeNode.right, level-1)

    #已知树的深度，按层遍历输出树的值
    def PrintNodeByLevel(self,treeNode, depth):
        for level in range(depth):
            self.PrintNodeAtLevel(treeNode,level)


pre = [1, 2, 3, 5, 6, 4]
tin = [5, 3, 6, 2, 4, 1]
test = Solution()
newTree = test.reConstructBinaryTree(pre, tin)
test.PrintNodeByLevel(newTree, 5)

