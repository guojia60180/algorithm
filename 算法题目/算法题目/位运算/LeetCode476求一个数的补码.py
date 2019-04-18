#Author guo
class Solution:
    def findComplement(self, num):
        v=[]
        s=bin(num)
        for i in range(2,len(s)):
                v.append(s[i])

        for i in range(len(v)):
            if v[i]=='1':
                v[i]='0'
            else:
                v[i]='1'
        s2=''.join(v)
        t=int(s2,2)
        return t#字符串处理方法

    def findComplement1(self, num):
        if num==0:
            return 1
        mask=1<<30
        while num&mask==0:
            mask>>=1
        mask=(mask<<1)-1
        return num^mask
    '''
    对于 00000101，要求补码可以将它与 00000111 进行异或操作。
    那么问题就转换为求掩码00000111'''
