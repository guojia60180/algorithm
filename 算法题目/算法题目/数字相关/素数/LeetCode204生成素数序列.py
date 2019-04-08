#Author guo
#素数筛选法
#找到一个素数，把这个数的倍数都删除
#最后统计没有被删除的个数

class Solution:
    def countPrimes(self, n):
       nums=[True]*n
       for i in range(2,n):
           j=2
           while i*j<n:
               nums[i*j]=False
               j=j+1
       res=0
       for i in range(2,n):
           if nums[i]:
               res+=1

       return res