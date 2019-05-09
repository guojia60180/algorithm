#Author guo
# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        s = []
        for i in range(1,n+1):

            s.append(str(i))
        x=''
        x=''.join(s)
        #print(x)
        return str(s).count('1')

    def NumberOf1Between1AndN_Solution1(self, n):
        ones=0
        m=1
        while m<n:
            ones+=(n//m+8)//10*m+(n // m % 10 == 1) * (n % m + 1)
            m*=10
        return ones

    def NumberOf1Between1AndN_Solution2(self, n):
        number=0
        for i in range(n+1):
            number+=self.NumberOf1(i)
        return number

    def NumberOf1(self,n):
        number=0
        while n:
            if n%10==1:
                number+=1
            n=n//10

        return number
c=Solution()
print(c.NumberOf1Between1AndN_Solution(10))