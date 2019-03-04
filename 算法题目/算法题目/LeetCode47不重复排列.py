#Author guo
class Solution:
    def permuteUnique(self, nums):
        res,visited=[],[0]*len(nums)
        nums.sort()
        self.dfs(nums,visited,[],res)
        return res



    def dfs(self,nums,visited,path,res):
        if len(nums)==len(path):
            res.append(path)
            return
        for i in range(len(nums)):
            if visited[i]==0:
                if i>0 and visited[i-1]==0 and nums[i]==nums[i-1]:
                    continue#确保了不重复，向后移动
                visited[i]=1
                self.dfs(nums,visited,path+[nums[i]],res)
                visited[i]=0
