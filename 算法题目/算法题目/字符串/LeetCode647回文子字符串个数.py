#Author guo
class Solution:
    def countSubstrings(self, s):
        '''
        对于单个字符，本身就是一个回文，对回文是奇数的情况进行遍历
        使用left和right双指针，往两边走，判断长度是3,4,5,7的子串是不是回文
        left和right两个指针指向字符相等
        再对回文是偶数情况同样遍历
        :param s: 
        :return: 
        '''
        count=0
        for i in range(len(s)):
            count+=1
            #回文数奇数
            left=i-1
            right=i+1
            while left>=0 and right<len(s) and s[left]==s[right]:
                count+=1
                left-=1
                right+=1
            #回文数时偶数
            left=i
            right=i+1
            while left>=0 and right<len(s) and s[left]==s[right]:
                count+=1
                left-=1
                right+=1

        return count

class Solution:
    def countSubstrings2(self, s):
        '''
        动态规划
        先确定所有的回文，string[start:end]是回文
        当确定string[i:j]是不是回文时
        1.string[i]==string[j]
        2.string[i+1:j-1]是回文吗
        :param s: 
        :return: 
        '''
        n=len(s)
        count=0
        start,end,maxL=0,0,0
        dp=[[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(i):
                dp[j][i]=(s[j]==s[i])&((i-j<2)|dp[j+1][i-1])
                if dp[j][i]:
                    count+=1
            dp[i][i]=1
            count+=1
        return count
