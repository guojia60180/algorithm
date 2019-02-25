#Author guo
class Soultion:
    def length_of_subStr(self,s):
        result=0
        dic={}
        quick=slow=0
        length=len(s)

        while quick!=length:
            if s[quick] in dic and slow<=dic[s[quick]]:
                slow=dic[s[quick]]+1
            else:
                result=max(result,quick-slow+1)
            dic[s[quick]]=quick

         #两个指针，一个快一个满，当快指针碰到与慢指针指向相同的字符时，更新满指针
            #迭代的是最小长度

            quick+=1
        return result