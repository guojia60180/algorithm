#Author guo
'''
对于”226”：

令dp数组为[0,0,0,0]，初始化为[1,0,0,0]；

从第一个位置开始，输入为”2”，不为”0”，所以dp数组为[1,1,0,0]；

第2个位置，输入为”2”，不为”0”，所以dp数组为[1,1,1,0]；此时前两位数字是”22”，满足区间，所以变为[1,1,2,0]；

第3个位置，输入为”6”，不为”0”，所以dp数组为[1,1,2,2]；此时前两位数字是”26”，满足区间，所以变为[1,1,2,3]。
--------------------- 

'''
class Solution:
    def numDecodings(self, s):
        dp=[0]*(len(s))
        dp[0]=1
        for i in range(1,len(dp)):
            if s[i-1]!='0':
                dp[i]=dp[i-1]
            if i !=1 and '09'<s[i-2:i]<'27':
                dp[i]=dp[i]+dp[i-2]

        return dp[-1]


