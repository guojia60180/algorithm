#Author guo
'''
广度优先遍历，每一层得到的所有新节点，要用队列存储被下一层遍历

深度优先遍历得到一个新节点后立马对新节点进行遍历

使用DFS对一个图进行遍历，能够遍历到的点都是可达的

栈 用来保存当前节点信息，当遍历新节点时返回时能够继续遍历当前节点
可以使用递归栈

标记 和BFS一样，同样需要对已经遍历过的节点进行标记


'''
class Solution:
    def maxAreaOfIsland(self, grid):
        maxArea=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]!=0:
                    maxArea=max(maxArea,self.AreaofIsland(grid,i,j))

        return maxArea

    def AreaofIsland(self,grid,i,j):
        if i>=0 and i<len(grid) and j>=0 and j<len(grid[0]) and grid[i][j]!=0:
            grid[i][j]=0
            return 1+self.AreaofIsland(grid,i+1,j)+self.AreaofIsland(grid,i+1,j)+self.AreaofIsland(grid,i-1,j)+self.AreaofIsland(grid,i,j+1)+self.AreaofIsland(grid,i,j-1)
        return 0


