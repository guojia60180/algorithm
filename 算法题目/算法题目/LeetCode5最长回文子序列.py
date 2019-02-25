#Author guo
class Solution:
    def longestPalindrome(self, s: str) -> str:
        result=''
        for i in range(len(s)):
            tmp=self.palindrome(s,i,i)
            if len(tmp)>len(result):
                result=tmp

            tmp=self.palindrome(s,i,i+1)
            if len(tmp)>len(result):
                result=tmp
        return result

#判断是否是回文序列
    def palindrome(self,s,l,r):
        while l>=0 and r<=len(s) and s[l]==s[r]:
            l=l-1
            r=r+1
        return s[l+1:r]