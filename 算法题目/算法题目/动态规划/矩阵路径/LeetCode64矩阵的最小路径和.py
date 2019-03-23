#Author guo
class Solution:
    def minPathSum(self, grid):
        if len(grid)==0 or len(grid[0])==0:
            return 0

        m=len(grid)
        n=len(grid[0])
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    before = 0
                elif i == 0:
                    before = grid[i][j - 1]
                elif j == 0:
                    before = grid[i - 1][j]
                else:
                    before = min(grid[i - 1][j], grid[i][j - 1])
                grid[i][j] = before + grid[i][j]#更新值
        return grid[m - 1][n - 1]#回到左下右下的值

