#Author guo
#汉明距离
class Solution:
    '''
    对两个数进行异或，统计多少个1
    '''
    def hammingDistance(self, x, y):
        z=x^y
        cnt=0
        while z!=0:
            if ((z&1)==0):
                cnt+=1
            z=z//2
        return cnt

    def hammingDistance1(self, x, y):
        z=x^y
        cnt=0
        while z!=0:
            z&=(z-1)#去除位最低的一位
            cnt+=1
        return cnt

    def hammingDistance2(self, x, y):
        return bin(x^y).count('1')