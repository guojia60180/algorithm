#Author guo
# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        '''
        建立一个辅助栈，把push序列的数字依次压入辅助栈，
        每次压入后，比较辅助栈的栈顶元素和pop序列的首元素是否相等，
        相等的话就推出pop序列的首元素和辅助栈的栈顶元素，
        若最后辅助栈为空，则push序列可以对应于pop序列。
        :param pushV: 
        :param popV: 
        :return: 
        '''
        stack=[]

        if not pushV and not popV:
            return True
        if not pushV and popV:
            return False
        if pushV and not popV:
            return False

        for i in pushV:
            stack.append(i)
            while stack[-1]==popV[0] and len(stack):
                stack.pop()
                popV.pop(0)


        # while len(stack)>0 and stack[-1]==popV[0]:
        #     stack.pop()
        #     popV.pop(0)
        if len(stack)==0:
            return True
        else:
            return False




