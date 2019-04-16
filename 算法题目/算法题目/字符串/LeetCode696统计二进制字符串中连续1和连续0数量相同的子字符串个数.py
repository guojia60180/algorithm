#Author guo
class Solution:
    def countBinarySubstrings2(self, s):
        #暴力解法
        #从每个位置开始向后数，数到0的个数和1的个数相等时停止
        #每次不用遍历到结尾 最坏的时间复杂度O[n^2]
        N=len(s)
        res=0
        for i in range(N):
            c1,c0=0,0
            if s[i]=='1':
                c1=1
            else:
                c0=1
            for j in range(i+1,N):
                if s[j]=='1':
                    c1+=1
                else:
                    c0+=1
                if c0==c1:
                    res+=1
                    break
        return res

    def countBinarySubstrings(self, s):
        #连续子串计算，数下连续0,1的个数有多少，构成一个数组
        #求得到0,1相等的子串，需要交错，找出相邻的两个个数的最小值
        #最后求的交错的最小值，就得到相邻字符串0,1相等的长度
        N=len(s)
        cur=1
        res=[]
        for i in range(1,N):
            if s[i]==s[i-1]:
                cur+=1
            else:
                res.append(cur)
                cur=1#初始化一下

        res.append(cur)
        return sum(min(x,y) for x,y in zip(res[:-1],res[1:]))
    '''
    分步来看
    1.res[:-1],res[1:] 两个切片分别为0-倒数第二 1-倒数第一
    2.zip 打包成为元组[(res[0],res[1]),(res[1],res[2]),()]这种形式
    3.求交错的最小值
    4.对求出的交错值进行叠加，求出总的个数
'''
    def countBinarySubstrings3(self, s):
        '''
        对于“当前位置”的数字来说，就只需要关注其“紧邻之前”有多少个相同数字，以及有多少个不同数字就好了。
        比如，当处理到00110时，对于最后一个0来说，只需要关注前面有没有1个1，这时10就是满足条件的子串；
        而当处理到001100时，对于最后一个0来说，它是第2个0，而其前面有2个1，这时1100就是满足条件的子串；
        再当处理到0011000时，对于最后一个0来说，它是第3个0，而其前面只有2个1，所以子串11000不满足条件。
 
        '''
        res=0
        prev_len=0
        cur_len=1
        for i in range(1,len(s)):
            if (s[i]==s[i-1]):
                cur_len+=1
            else:
                prev_len=cur_len
                cur_len=1

            if prev_len>=cur_len:
                res+=1

        return res