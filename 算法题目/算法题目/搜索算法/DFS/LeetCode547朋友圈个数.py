#Author guo
class Solution:
    def findCircleNum(self, M):
        n=len(M)
        res=0
        visited=[0]*len(M)
        for i in range(n):
            if not visited[i]:
                visited[i]=1
                self.dfs(M,visited,i)
                res=res+1

        return res

    def dfs(self,M,visited,i):
        for j in range(len(M)):
            if M[i][j] and not visited[j]:
                visited[j]=1
                self.dfs(M,visited,j)
#visited 则是因为a[i][j]=a[j][i]