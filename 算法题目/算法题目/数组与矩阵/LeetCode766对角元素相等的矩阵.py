#Author guo
#以对角线分开两块，左上块与右下块如果包含的数字是相同的
#则认为是对称的矩阵

class Solution:
    def isToeplitzMatrix(self, matrix):
        for row in range(len(matrix)-1):
            for col in range(len(matrix[0])-1):
                if matrix[row][col]!=matrix[row+1][col+1]:
                    return False

        return True
#当前的与它的行偏移一个，列偏移一个相等
#就可以完成