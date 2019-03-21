#Author guo
class Solution:
    def combine(self, n, k):
        res=[]
        self.dfs(res,0,n,k,[])
        return res

    def dfs(self,res,i,n,k,temp):
        if k==0:
            res.append(temp)
            return
        for j in range(i+1,n+1):
            self.dfs(res,j,n,k-1,temp+[j])
#注意起始于终止条件