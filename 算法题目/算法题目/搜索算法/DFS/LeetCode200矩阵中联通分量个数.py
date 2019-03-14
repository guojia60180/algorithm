#Author guo
class Solution:
    def numIslands(self, grid):
        res=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    self.Island(grid,i,j)
                    res=res+1
        return res
    def Island(self,grid,i,j):
        dirs=[[-1,0],[0,1],[0,-1],[1,0]]
        grid[i][j]='0'
        for dir in dirs:
            r=i+dir[0]
            c=j+dir[1]
            if r>=0 and c>=0 and r<len(grid) and c<len(grid[0]):
                if grid[r][c]=='1':
                    self.Island(grid,r,c)