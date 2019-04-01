#Author guo
#转换为最长公共子序列
class Solution:
    def minDistance(self, word1, word2):
        dp=[[0]*(len(word2)+1)for _ in range(len(word1)+1)]
        for i in range (1,len(word1)+1):
            for j in range(1,len(word2)+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i][j-1],dp[i-1][j])

        val=dp[-1][-1]
        return len(word2)+len(word1)-val*2
