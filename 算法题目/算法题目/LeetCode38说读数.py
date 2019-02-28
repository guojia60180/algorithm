#Author guo
class Solution:
    def countAndSay(self, n):
        s='1'

        for i in range(n-1):
            a=s[0]
            temp=''
            count=0
            for l in s:
                if a==l:
                    count=count+1#如果说的一个与之前的相同，计数器加1
                else:
                    temp=temp+str(count)+a
                    a=l
                    count=1
            temp=temp+str(count)+a
            s=temp
        return s