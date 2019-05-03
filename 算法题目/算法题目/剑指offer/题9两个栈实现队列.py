#Author guo
# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        # write code here
        self.stack1.append(node)

    def pop(self):
        # return xx
        if self.stack2 == None and self.stack1 == None:
            return

        elif self.stack2 == []:
            while self.stack1 != []:
                self.stack2.append(self.stack1.pop())

        return self.stack2.pop()