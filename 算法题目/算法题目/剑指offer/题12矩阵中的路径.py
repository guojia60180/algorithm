#Author guo
# -*- coding:utf-8 -*-
'''
判断矩阵中是否存在一条包含某字符串所有字符的路径
'''
'''
回溯法
任选一个格子作为路径的起点，假设矩阵中某个格子的字符为ch，且这个格子
对应路径上第i个字符，如果第i个字符不是ch，这个格子不可能处在路径上第i个位置
如果第i个字符刚好是ch。往相邻的格子寻找路径的第i+1个字符
除在边界的格子外，其他各自都有四个相邻的格子，重复过程直到路径上所有字符都在矩阵中找到相应位置

'''
# -*- coding:utf-8 -*-
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        if not matrix and rows <= 0 and cols <= 0 and path == None:
            return False
        # 模拟的字符矩阵
        markmatrix = [0] * (rows * cols)
        pathlength = 0
        # 从第一个开始递归，当然第一二个字符可能并不位于字符串之上，所以有这样一个双层循环找起点用的，一旦找到第一个符合的字符串，就开始进入递归，
        # 返回的第一个return Ture就直接跳出循环了。
        for row in range(rows):
            for col in range(cols):
                if self.hasPathCore(matrix, rows, cols, row, col, path, pathlength, markmatrix):
                    return True
        return False

    def hasPathCore(self, matrix, rows, cols, row, col, path, pathlength, markmatrix):
        # 说明已经找到该路径，可以返回True
        if len(path) == pathlength:
            return True

        hasPath = False
        if row >= 0 and row < rows and col >= 0 and col < cols and matrix[row * cols + col] == path[pathlength] and not \
                markmatrix[row * cols + col]:
            pathlength += 1
            markmatrix[row * cols + col] = True
            # 进行该值上下左右的递归
            hasPath = self.hasPathCore(matrix, rows, cols, row - 1, col, path, pathlength, markmatrix) \
                      or self.hasPathCore(matrix, rows, cols, row, col - 1, path, pathlength, markmatrix) \
                      or self.hasPathCore(matrix, rows, cols, row + 1, col, path, pathlength, markmatrix) \
                      or self.hasPathCore(matrix, rows, cols, row, col + 1, path, pathlength, markmatrix)

            # 对标记矩阵进行布尔值标记
            if not hasPath:
                pathlength -= 1
                markmatrix[row * cols + col] = False
        return hasPath