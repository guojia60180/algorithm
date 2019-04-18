#Author guo
class Solution:
    def isPowerOfTwo(self, n):
        if n<0:
            return False
        #把该数字用二进制表示，只有一个1
        return bin(n).count('1')==1

    #利用该数字与该数字-1的两个值做相与==0来得到
    def isPowerOfTwo2(self, n):
        return n>0 and (n&(n-1))==0
