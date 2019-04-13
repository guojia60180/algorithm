#Author guo
#层次遍历
#[1 2 3 4 5 6] 一层一层遍历
#前序遍历
#[1 2 4 5 3 6] 中左右
#中序遍历
#[4 2 5 1 3 6] 左中右
#后序遍历
#[4 5 2 6 3 1] 左右中

'''
层次遍历使用BFS实现，利用BFS一层一层遍历的特性
前序，中序，后序使用DFS实现

前后中只是对节点访问顺序有不同
'''

#前序
class async:
    def dfs(self,root):
        self.visit()
        self.dfs(root.left)
        self.dfs(root.right)
    #中序
    def dfs(self,root):
        self.dfs(root.left)
        self.visit()
        self.dfs(root.right)
    #后序
    def dfs(self,root):
        self.dfs(root.left)
        self.dfs(root.right)
        self.visit()