#Author guo
class Solution:
    def subsets(self, nums):
        if nums==None:
            return []
        res=[]
        self.dfs(0,sorted(nums),res,[])
        return res

    def dfs(self,i,nums,res,subsetres):
        res.append(subsetres)
        for j in range(i,len(nums)):
            self.dfs(j+1,nums,res,subsetres+[nums[j]])