#Author guo
class Solution:
    # @param n, an integer
    # @return an integer
    '''
    参考于十进制转二进制，我们手动计算时，都是每次除以2，
    取余数，然后将所有余数翻转即为二进制数，既然要翻转其二进制，
    那再转换二进制时，就不用翻转余数了，
    直接利用余数求出新的翻转后的十进制就可以。

例如：10，二进制是1010，10%2=0，5%2=1，2%2=0,1%2=1，
所以是倒叙1010，然后在取余的过程中，直接从2的31次方开始算起。 
0*2^31+1*2^30+0*29+1*2^28即为翻转二进制后的十进制数。
--------------------- 

    '''
    def reverseBits(self, n):
       v=[]
       while n>0:
           v.append(n%2)
           n=n//2
       a=0
       for i in range(len(v)):
           a=a+pow(2,31-i)*v[i]
       return int(a)