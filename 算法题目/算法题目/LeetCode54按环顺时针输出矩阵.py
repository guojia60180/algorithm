#Author guo
class Solution:
    def spiralOrder(self, matrix):
        # 一步一步走
        if not matrix:
            return []
        up = left = 0
        down = len(matrix) - 1  # 列数
        right = len(matrix[0]) - 1  # 行数

        direct = 0  # 方向设置
        res = []
        while True:
            if direct == 0:
                for i in range(left, right + 1):
                    res.append(matrix[up][i])
                up = up + 1

            if direct == 1:
                for i in range(up, down + 1):
                    res.append(matrix[i][right])
                right = right - 1

            if direct == 2:
                for i in range(right, left - 1, -1):
                    res.append(matrix[down][i])
                down = down - 1

            if direct == 3:
                for i in range(down, up - 1, -1):
                    res.append(matrix[i][left])
                left = left + 1

            if up > down or left > right:
                return res

            direct = (direct + 1) % 4
