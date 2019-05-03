#Author guo
'''
长度n的绳子，剪成m段，使m段的绳子乘积最大
'''

class Solution:
    def cut(self,n):
        x=n%3
        y=n//3
        if x==0:
            return pow(3,y)
        elif x==1:
            y=y-1
            return pow(3,y)*4
        else:
            return pow(3,y)*2
    def maxproductAfterCutting(self,n):
        if n<2:
            return 0
        if n==2:
            return 1
        if n==3:
            return 2

        products=[0]*(n+1)
        products[0]=0
        products[1]=1
        products[2] =2
        products[3] = 3
        max=0
        for i in range(4,n+1):
            max=0
            for j in range(1,i//2+1):
                product=products[j]*products[i-j]
                if max<product:
                    max=product
                products[i]=max
        max=products[n]

        return max

test=Solution()
print(test.maxproductAfterCutting(6))
