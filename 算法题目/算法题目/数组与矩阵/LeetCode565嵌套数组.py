#Author guo
class Solution:
    def arrayNesting(self, nums):
        '''
        给出一个数组，从任意位置出发，把该位置数字当做下一个索引的位置
        最后肯定会终止环路
        :param nums: 
        :return: 
        '''
        #思路简单，利用数组保存某个位置是否访问
        #如果遇到访问的，终止并记录

        visited=[False]*len(nums)
        ans=0
        for i in range(len(nums)):
            road=0
            while not visited[i]:
                road+=1

                visited[i]=True
                i=nums[i]
            ans=max(ans,road)
        return ans