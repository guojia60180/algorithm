#Author guo
class Solution:
    def longestPalindrome(self, s):
        #字符有偶数个可以用来构成回文字符串
        #回文字符串中间的字符可以单独出现，单独字符就可以放在中间

        h={}
        for i in s:
            if i in h:
                h[i]+=1
            else:
                h[i]=1

        c=0
        sig=0
        for i in h:
            c+=h[i]//2
            if h[i]%2!=0:
                sig=1#单个字符的取出来算一个

        return c*2+sig
