#Author guo
'''
栈的顺序后进先出，队列先进先出，使用两个栈实现队列
一个元素经过两个栈才能出队列
经过第一个栈时，元素顺序反转
经过第二个栈时再被反转
此时先进先出
'''
class MyQueue:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.instack=[]
        self.outstack=[]

    def push(self, x):
        """
        Push element x to the back of queue.
        """
        self.instack.append(x)
    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.outstack:
            return self.outstack.pop()
        else:
            while self.instack:
                self.outstack.append(self.instack.pop())
            return self.outstack.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.outstack:
            return self.outstack[-1]
        else:
            while self.instack:
                self.outstack.append(self.instack.pop())
            return self.outstack[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.instack and not self.outstack



        # Your MyQueue object will be instantiated and called as such:
        # obj = MyQueue()
        # obj.push(x)
        # param_2 = obj.pop()
        # param_3 = obj.peek()
        # param_4 = obj.empty()