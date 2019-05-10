#Author guo
#1.先把数组中每一个数字异或 得到两个数字的异或
#2.找到这两个数字异或的最低位不一样的位置，区分两个数字
#3.分组，一个组分为最低位是1的，一组分为最低位是0的
#4,异或一个组的全部数，求出一个只出现一次的
#5，把一开始两个异或的数与求出的数异或
import collections


# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        a = 0
        if not array:
            return
        for x in array:
            a = a ^ x
        y = 0
        C = collections.Counter(array)
        for i,k in enumerate(C):
            if C[k] == 1:
                y = k

        res = [y, y ^ a]
        return res

    def FindNumsAppearOnce1(self, array):
        xor=0
        for x in array:
            xor=xor^x

        indexbits=0
        while xor&1==0:
            xor=xor>>1
            indexbits+=1#求出了最低不为1的位
        m=[]
        n=[]
        for x in array:
            if (x>>indexbits)&1==0:
                m.append(x)
            else:
                n.append(x)
        t=0
        for y in m:
           t=t^y

        s=0
        for z in n:
            s=s^z

        return [t,s]
        #分两组，每一组都有一个值，另外的都是重复两遍的



S=Solution()
print(S.FindNumsAppearOnce([4,6,1,1,1,1]))
