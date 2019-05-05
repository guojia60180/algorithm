#Author guo
# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        if exponent < 0:
            exponent = abs(exponent)
            res = 1
            for i in range(exponent):
                res = res * base
            return 1 / res  # 自带double类型，边界值的处理
        elif exponent == 0:
            return 1

        else:
            res = 1
            for i in range(exponent):
                res = res * base
            return res
'''
当n为偶数, a^n = a^(n/2) * a^(n/2)
当n为奇数, a^n = a^((n-1)/2) * a^((n-1)/2)) * a
利用右移一位运算代替除以2
利用位与运算代替了求余运算法%来判断一个数是奇数还是偶数
优化代码速度
'''
class Solution2:
    def Power(self, base, exponent):
        if exponent == 0:
            return 1
        if exponent == 1:
            return base
        if exponent == -1:
            return 1/base

        result = self.Power(base, exponent >> 1)#除以2
        result *= result
        if (exponent & 0x1) == 1:#求余运算，判断是否为奇数偶数
            result *= base
        return result

S = Solution2()
print(S.Power(5, -10))
