#Author guo
class Solution(object):
    def longestValidParentheses(self, s):
        stack=[]
        match=[0 for i in range(0,len(s))]
        for i,c in enumerate(s):
            if c=='(':
                stack.append(i)

            elif c==')' and len(stack)!=0:#确保其中有元素
                match[i]=match[stack[-1]]=1
                stack.pop()

        res,tmp=0,0
        for i,c in enumerate(match):
            if match[i]==1:
                tmp=tmp+1
                res=max(res,tmp)
            else:
                tmp=0
        return res

    #直接用个bool数组标记括号是否匹配，如果匹配为1，之后进行统计


