#Author guo
class Solution:
    def isPowerOfFour(self, num):
        #4的n次方在二进制表示中有且只有一个奇数位为1
        if num<=0:
            return False
        if num==1:
            return True
        if num%4==0:
            return self.isPowerOfFour(num//4)
        return False

    def isPowerOfFour2(self, num):

         return num > 0 and (num & (num - 1)) == 0 and (num & 0x55555555) != 0

