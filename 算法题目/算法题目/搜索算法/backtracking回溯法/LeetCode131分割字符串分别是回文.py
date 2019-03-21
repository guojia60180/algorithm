#Author guo
class Solution:
    def partition(self, s):
        self.ispalindrome=lambda s:s==s[::-1]
        res=[]
        self.dfs(s,res,[])
        return res

    def dfs(self,s,res,path):
        if not s:
            res.append(path)
            return
        for i in range(1,len(s)+1):
            if self.ispalindrome(s[:i]):
                self.dfs(s[i:],res,path+[s[:i]])