#Author guo
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):

        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root):
        res=[]
        pathlist=[]
        self.dfs(root,pathlist,res)
        return res

    def dfs(self,root,pathlist,res):
        if not root:
            return
        pathlist.append(str(root.val))
        if not root.left and not root.right:
            res.append('->'.join(pathlist))
        if root.left:
            self.dfs(root.left,pathlist,res)
        if root.right:
            self.dfs(root.right,pathlist,res)
        pathlist.pop()