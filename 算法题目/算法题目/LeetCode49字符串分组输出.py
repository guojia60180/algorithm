#Author guo
class Solution:
    def groupAnagrams(self, strs):
        dic={}
        for s in strs:
            a=list(s)
            #print(a)
            a.sort()
            #print(a)
            a=''.join(a)
            #print(a)
            if a not in dic:
                dic[a]=[s]#key值定义
                #print(dic)
            else:
                dic[a].append(s)

        result=[]
        for s in dic:
            dic[s].sort()
            result.append(dic[s])
        return result

f=Solution()
f.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])



