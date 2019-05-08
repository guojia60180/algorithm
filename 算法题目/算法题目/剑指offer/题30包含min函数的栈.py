#Author guo
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack=[]
        self.minstack=[]
    def push(self, node):
        self.stack.append(node)
        if self.minstack==[] or node<min(self.minstack):
            self.minstack.append(node)
        else:
            self.minstack.append(min(self.minstack))
        # write code here
    def pop(self):
        self.stack.pop()
        self.minstack.pop()
        # write code here
    def top(self):
        return self.stack[-1]
        # write code here
    def min(self):
        # write code here
        return self.minstack[-1]