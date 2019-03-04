#Author guo
import math


class Solution:
    def judgeSquareSum(self, c):  # 判断是否是两个数的平方和
        tem = int(math.sqrt(c))

        i = 0
        while i <= tem:
            res = i ** 2 + tem ** 2
            if res == c:
                return True
            elif res > c:
                tem = tem - 1
            else:
                i = i + 1

        return False



