#Author guo
class Solution:
    def isPalindrome(self, x):
        #两种，一种通过除法验证
        #一种通过字符串判断，逆序判断两个字符串是否相等
        if x < 0:
            return False

        '''
        p=str(x)

        tmp=p[::-1]
        if p==tmp:
            return True
        else:
            return False
        '''

        p = x
        res = 0
        while p:
            res = res * 10 + p % 10
            p = p // 10

        return res == x