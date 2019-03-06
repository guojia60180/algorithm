#Author guo
class Solution:
    def findContentChildren(self, g, s) :
        g=sorted(g)
        s=sorted(s)
        gi=0
        si=0
        while gi<len(g) and si<len(s):
            if g[gi]<=s[si]:
                gi+=1
            si+=1
        return gi
        #如果gi《=si 该孩子可以被满足，不过不行，则si+1
    #返回gi 就是孩子的序号