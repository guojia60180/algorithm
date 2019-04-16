#Author guo
class Solution:
    def isIsomorphic(self, s, t):
        #记录上一个字符出现位置，如果两个字符串中字符上次出现的位置一样，就属于同构
        S_index=[0]*256
        T_index=[0]*256
        for i in range(len(s)):
            sc=s[i]
            tc=t[i]
            if S_index[ord(sc)]!=T_index[ord(tc)]:
                return False

            S_index[ord(sc)]=i+1
            T_index[ord(tc)]=i+1

        return True
