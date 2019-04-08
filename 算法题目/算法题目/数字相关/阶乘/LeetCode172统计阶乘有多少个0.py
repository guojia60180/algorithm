#Author guo
class Solution:
    def trailingZeroes(self, n):
        #只要统计n中包含的5的个数
#其中25 125 之类的都多包含一遍 递归实现

        return 0 if n==0 else n//5+self.trailingZeroes(n//5)
