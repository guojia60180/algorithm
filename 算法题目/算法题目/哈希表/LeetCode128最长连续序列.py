#Author guo
class Solution:
    def longestConsecutive(self, nums):
        #建立字典做查询
        #哈希表存储连续数值的端点和对应的长度，这样如果新遍历的数左边或右边可以和已有的区间连上的话就可以对原有的区间进行扩张
        n=len(nums)
        d={}
        ans=0
        for i in nums:
            if i not in d:
                left=d.get(i-1,0)#没有的话设置默认值0
                right=d.get(i+1,0)
                length=left+right+1
                ans=max(ans,length)

                d[i]=length
                d[i-left]=length
                d[i+right]=length

        return ans