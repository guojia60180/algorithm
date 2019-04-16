#Author guo
'''
遍历数组时，用栈把数组中数存起来，如果当前遍历比栈顶元素大
说明栈顶元素的下一个比它大的数就是当前元素

'''
class Solution:
    def dailyTemperatures(self, T):
        n=len(T)
        res=[0]*n
        stack=[]#存两个元素，当前天+与今天的位置差
        for i,t in enumerate(T):
            while stack and stack[-1][0]<t:
                oi=stack.pop()[1]
                res[oi]=i-oi
            stack.append((t,i))

        return res