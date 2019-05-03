#Author guo
class Queue:
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return self.items==[]

    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()
    def dequeue2(self):
        return self.items.pop(0)
    def size(self):
        return len(self.items)

def hotpotato(namelist,num):
    simqueue=Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size()>1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())
        simqueue.dequeue()

    return simqueue.dequeue()
print(hotpotato(["Bill","David","Susan","Jane","Kent","Brad"],10))


#利用的确解决回文字符串

def palcker(string):
    chardeque=Queue()

    for ch in string:
        chardeque.enqueue(ch)

    stillEqual=True

    while chardeque.size()>1 and stillEqual:
        first=chardeque.dequeue()
        last=chardeque.dequeue2()
        if first!=last:
            stillEqual=False

    return stillEqual
print(palcker('lsdkjfskf'))
print(palcker('radar'))