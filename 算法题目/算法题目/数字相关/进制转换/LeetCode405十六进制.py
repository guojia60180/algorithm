#Author guo
#转化一个数从十进制到16进制

class Solution:
    def toHex(self, num):
        if num==0:
            return '0'
        res=''
        if num<0:
            num+=1<<32
        while num!=0:
            last=num%16
            if last<10:
                res=str(last)+res

            else:
                res=chr(last-10+ord('a'))+res

            num/=16

        return res
