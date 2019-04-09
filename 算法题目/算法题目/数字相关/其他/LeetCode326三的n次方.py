#Author guo
#判断是否是3的n次方
class Solution:
    def isPowerOfThree(self, n):
        return n>0 and (1162261467%n==0)