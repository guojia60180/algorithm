#Author guo
#利用一个辅助栈，保存目前为止的最小值来完成

class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack=[]
        self.minstack=[]
    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.minstack:
            self.minstack.append(x)
        else:
            self.minstack.append(min(self.minstack[-1],x))
    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()#最小值输出
    def top(self) -> int:
        return self.stack[-1]#最后一个值，栈顶
    def getMin(self) -> int:
        return self.minstack[-1]#最后最小的一个值
    # Your MinStack object will be instantiated and called as such:
    # obj = MinStack()
    # obj.push(x)
    # obj.pop()
    # param_3 = obj.top()
    # param_4 = obj.getMin()