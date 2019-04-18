#Author guo
'''
既然不能使用加法和减法，那么就用位操作。下面以计算5+4的例子说明如何用位操作实现加法： 
1. 用二进制表示两个加数，a=5=0101，b=4=0100； 
2. 用and（&）操作得到所有位上的进位carry=0100; 
3. 用xor（^）操作找到a和b不同的位，赋值给a，a=0001； 
4. 将进位carry左移一位，赋值给b，b=1000； 
5. 循环直到进位carry为0，此时得到a=1001，即最后的sum。



'''
#python中一直左移是不会溢出的，所以要手动模拟32位int型
class Solution:
    def getSum(self, a, b):
        MAX_INT=0x7FFFFFFF
        MIN_INT=MAX_INT+1
        Mask=0x100000000#2^32 1-32位上都是1
        while b!=0:
            carry=(a&b)<<1 #进位
            a=(a^b)%Mask#取余，把范围限制在【0-2^32】内
            b=carry%Mask

        return a if a<=MAX_INT else ~((a%MIN_INT)^MAX_INT)
#小于max——int 不需要处理

