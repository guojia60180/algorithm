#Author guo
# -*- coding:utf-8 -*-
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
class Solution:
    def Serialize(self, root):
        # write code here
        string=''
        if root==None:
            return '#'
        stack=[]
        while root or stack:
            while root:
                string=string+str(root.val)+','
                stack.append(root)
                root=root.left
            string=string+'#,'
            root=stack.pop()
            root=root.right
        string=string[:-1]
        return string
    def Deserialize(self, s):
        # write code here
        string=s.split(',')
        tree,sp=self.deserialize(string,0)
        return tree

    def deserialize(self,s,sp):
        if sp>len(s) or s[sp]=='#':
            return None,sp+1
        node = TreeNode(int(s[sp]))

        sp+=1
        node.left,sp=self.deserialize(s,sp)
        node.right,sp=self.deserialize(s,sp)

        return node,sp