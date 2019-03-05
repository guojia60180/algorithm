#Author guo
class Solution:
    def frequencySort(self, s):
        dic={}
        res=''

        for char in s:
            if char in dic:
                dic[char]+=1
            else:
                dic[char]=1

        sorted_dic=sorted(dic,key=dic.get,reverse=True)

        for count in sorted_dic:
            res=res+count*(dic[count])#res=每个数乘以该键值出现的次数
        return res