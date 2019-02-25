#Author guo
class Soultion:
    def two_sum(self,nums,target):
        list=[]
        n=len(nums)
        for i in range(n):
            x=target-nums[i]
            if x in nums and nums.index(x)!=i:
                return [i,nums.index(x)]

'''
思路通过找index的值，来找到两个数可以相加等于index的
'''

