#Author guo
class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        if threshold<0 or rows<=0 or cols<=0:
            return 0
        visited=[0]*(rows*cols)
        for i in range(rows*cols):
            visited[i]=False
        count=self.movingCountCore(threshold,rows,cols,0,0,visited)

        return count
    def movingCountCore(self,threshold,rows,cols,row,col,visited):
        count=0
        if self.check(threshold,rows,cols,row,col,visited):
            visited[row*cols+col]=True

            count=1+self.movingCountCore(threshold,rows,cols,row-1,col,visited)+self.movingCountCore(threshold,rows,cols,row+1,col,visited)+self.movingCountCore(threshold,rows,cols,row,col+1,visited)+self.movingCountCore(threshold,rows,cols,row,col-1,visited)

        return count
    def getdigitsum(self,number):
        sum=0
        while number>0:
            sum=sum+number%10
            number=number//10

        return sum

    def check(self,threshold,rows,cols,row,col,visited):
        if row>=0 and row<rows and col>=0 and col<cols and self.getdigitsum(row)+self.getdigitsum(col)<=threshold and not visited[row*cols+col]:
            return True

        return False

s = Solution()
print(s.movingCount(5, 10, 10))
