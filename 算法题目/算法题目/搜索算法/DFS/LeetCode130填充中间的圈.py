#Author guo
class Solution:
    m, n = 0, 0
    dirs = [[-1, 0], [0, 1], [0, -1], [1, 0]]
    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        #从外至内填充，逐步的填充完


        if board==None or len(board)==0:
            return

        m=len(board)
        n=len(board[0])

        for i in range(m):
            self.dfs(board,i,0)
            self.dfs(board,i,n-1)

        for i in range(n):
            self.dfs(board,0,i)
            self.dfs(board,m-1,i)

        for i in range(m):
            for j in range(n):
                if board[i][j]=='T':
                    board[i][j]='O'
                elif board[i][j]=='O':
                    board[i][j]='X'


    def dfs(self,board,r,c):
        m, n = 0, 0
        m=len(board)
        n=len(board[0])
        dirs = [[-1, 0], [0, 1], [0, -1], [1, 0]]
        if r<0 or r>=m or c<0 or c>=n or board[r][c]!='O':
            return
        board[r][c]='T'
        for dir in dirs:
            self.dfs(board,r+dir[0],c+dir[1])