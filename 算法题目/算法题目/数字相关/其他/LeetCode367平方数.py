#Author guo
#判断是否是完全平方数
class Solution:
    def isPerfectSquare(self, num):
        #平方数之间差为3，5,7,9
        subnumber=1
        while num>0:
            num=num-subnumber
            subnumber+=2

        return num==0

