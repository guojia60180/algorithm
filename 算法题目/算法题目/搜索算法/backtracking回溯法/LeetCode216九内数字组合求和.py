#Author guo
class Solution:
    def combinationSum3(self, k, n):
        res=[]
        self.dfs(res,0,k,n,[],range(1,10))
        #迭代初始
        return res


    def dfs(self,res,index,k,n,path,nums):
        if k==0 and n==0:
            res.append(path)
            return

        for i in range(index,len(nums)):
            self.dfs(res,i+1,k-1,n-nums[i],path+[nums[i]],nums)

#每次迭代的方式
