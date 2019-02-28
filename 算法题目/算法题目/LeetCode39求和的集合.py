#Author guo

class Solution:
    def combinationSum(self, candidates, target):
        candidates=sorted(candidates)
        res=[]
        self.dfs(candidates,target,0,[],res)
        return res

    def dfs(self,candidates,target,index,path,res):
        if target==0:
            res.append(path)
            return#结果添加的过程
        if target<candidates[0]:
            return

        for i in range(index,len(candidates)):
            self.dfs(candidates,target-candidates[i],i,path+[candidates[i]],res)

#递归的方式