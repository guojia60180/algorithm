#Author guo
class Solution:
    def rotate(self, matrix):
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for row in matrix:
            for j in range(len(matrix)//2):
                row[j],row[len(matrix)-j-1]=row[len(matrix)-j-1],row[j]