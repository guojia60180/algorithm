#Author guo
class Solution:
    def combinationSum2(self, candidates, target):
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
            if i!=index and candidates[i] == candidates[i-1]:#假设第i个与第i-1个相同
                    continue
            self.dfs(candidates,target-candidates[i],i+1,path+[candidates[i]],res)#目标-candidates[i] 路径加上一个该当前值
            #注意跳过了第i个，向后