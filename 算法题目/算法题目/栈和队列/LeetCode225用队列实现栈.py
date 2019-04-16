#Author guo
'''
在将元素x插入队列时，为了维护原来的先后顺序
需要x插入队列首部
队列默认插入顺序是队列尾部
因此在插入队列尾部后，需要让除x之外对的所有元素出队列，再入队列
'''

#使用一个队列完成
#每次新元素进入队列，先把当前数字进入队列，然后再把前面所有元素翻转一下
#翻转到元素后面
import collections
class MyStack:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.que=collections.deque()
    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.que.append(x)
        for i in range(len(self.que)-1):
            self.que.append(self.que.popleft())
    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.que.popleft()
    def top(self) -> int:
        """
        Get the top element.
        """
        return self.que[0]
    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.que


        # Your MyStack object will be instantiated and called as such:
        # obj = MyStack()
        # obj.push(x)
        # param_2 = obj.pop()
        # param_3 = obj.top()
        # param_4 = obj.empty()