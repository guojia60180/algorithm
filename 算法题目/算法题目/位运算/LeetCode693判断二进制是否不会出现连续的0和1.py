#Author guo
class Solution:
    def hasAlternatingBits(self, n):
        #对于1010这种数，把它右移1位得到101，这两个数每个位都不同
#异或得到1111 依次异或得到111
        a=(n^(n>>1))#看是否是1111
        return a&(a+1)==0#如果全为1，那么+1后与其相与就全是0