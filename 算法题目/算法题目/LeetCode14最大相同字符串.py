#Author guo
class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs)<1:return ''

        elif len(strs)==1:return strs[0]#如果只有一个返回第一个

        s=strs[0]

        for i in range(1,len(strs)):
            l=min(len(s),len(strs[i]))
            while strs[i][:l]!=s[:l]:#如果两者不相等使得长度-1

                l=l-1
            s=s[:l]

        return s



