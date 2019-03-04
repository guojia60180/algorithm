#Author guo
#至多删除一个字符，剩下的是回文序列
class Solution:
    def validPalindrome(self, s):
        left,right=0,len(s)-1
        while left<right:
            if s[left]!=s[right]:
                a,b=s[left:right],s[left+1:right+1]
                return a==a[::-1] or b==b[::-1]#比较逆序，其中+1是可以删除一个元素

            left,right=left+1,right-1

        return True

