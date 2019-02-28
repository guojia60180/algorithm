#Author guo
class Solution:
    def isValidSudoku(self, board):
        r,c=len(board),len(board[0])
        for i in range(r):
            for j in range(c):
                if not self.isvalid(i,j,board):
                    return False

        return True



    def isvalid(self,x,y,board):
        if board[x][y]=='.':
            return True
        tmp=board[x][y]
        board[x][y]='#'
        r, c = len(board), len(board[0])
        for i in range(r):
            if board[i][y]==tmp:
                return False#有重复的元素
        for j in range(c):
            if board[x][j]==tmp:
                return  False

        for i in range(x//3*3,x//3*3+3):
            for j in range(y//3*3,y//3*3+3):
                if board[i][j]==tmp:
                    return False
        board[x][y]=tmp
        return True

#分成两部分，一部分用来说明该格子是否可以，判断依据是行中有重复，列中
#you重复，再判断3*3的格子里是否有重复，这里利用了整除的方式，没有最优化