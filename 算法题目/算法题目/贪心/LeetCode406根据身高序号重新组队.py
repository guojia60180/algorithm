#Author guo
#身高高的同学先进行插入，身高降序，k值增序，按照排好的顺序插入k位置

class Solution:
    def reconstructQueue(self, people):
        if not people:
            return []

        dic={}
        height=[]
        res=[]

        for i in range(len(people)):
            p=people[i]

            if p[0] in dic:
                dic[p[0]]+=(p[1],i)
            else:
                dic[p[0]]=[(p[1],i)]
                height=height+p[0]

        height.sort()

        for h in height[::-1]:
            dic[h].sort()
            for p in dic[h]:
                res.insert(p[0],people[p[1]])
        return res
