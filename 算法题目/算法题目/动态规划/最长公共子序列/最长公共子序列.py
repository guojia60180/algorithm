#Author guo
'''
动态规划想法
定义二维数组dp[i][j]用来存储最长公共子序列的长度

其中dp[i][j]表示S1前i个字符与S2前j个字符最长公共子序列长度
考虑S1i与S2j是否值相等分为两种情况

相等时，dp[i][j]=dp[i-1][j-2]+1
不相等时，取最大值

'''
#递归
def recursive_lcs(stra,strb):
    if len(stra)==0 or len(strb)==0:
        return 0
    if stra[0]==strb[0]:
        return recursive_lcs(stra[1:],strb[1:])+1
    else:
        return max([recursive_lcs(stra[1:],strb),recursive_lcs(stra,strb[1:])])

#动态规划
def lcs(stra,strb):
    m=[[0 for i in range(len(strb)+1)]for j in range(len(stra)+1)]
    mmax=0
    p=0#最长匹配中对应在stra的最后一位
    for i in range(len(stra)):
        for j in range(len(strb)):
            if stra[i]==strb[j]:
                m[i+1][j+1]=m[i][j]+1
                if m[i+1][j+1]>mmax:
                    mmax=m[i+1][j+1]
                    p=i+1
    return stra[p-mmax:p],mmax
