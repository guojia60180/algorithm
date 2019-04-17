#Author guo
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix==None or len(matrix)==0 or len(matrix[0])==0:
            return False
        m=len(matrix)
        n=len(matrix[0])
        row=0
        col=n-1
        while row<m and col>=0:
            if target==matrix[row][col]:
                return True
            elif target<matrix[row][col]:
                col-=1
            else:
                row+=1

        return False