#Author guo
class Node:
    def __init__(self,initdata):
        self.data=initdata
        self.next=None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newData):
        self.next=newData

    def setNext(self,nextNode):
        self.next=nextNode

temp=Node(30)
temp.setData(29)
print(temp.getNext())

#定义一个无序列表

class UnorderedList:
    def __init__(self):
        self.head=None
    def show(self):
        res=[]
        current = self.head
        while current!=None:
            res.append(current.data)
            current=current.getNext()

        return res
    def isEmpty(self):
        return self.head==None

    def add(self,item):
        temp=Node(item)
        temp.setNext(self.head)
        self.head=temp

    def size(self):
        current=self.head
        count=0
        while current!=None:
            count+=1
            current=current.getNext()

        return count

    def search(self,item):
        current=self.head
        found=False
        while current!=None and found==False:
            if current.getData()==item:
                found=True
            else:
                current=current.getNext()
        return found

    def remove(self,item):
        current=self.head
        pre=None
        found=False
        while current!=None and not found:
            if current.getData()==item:
                found=True
            else:
                pre=current
                current=current.getNext()
        if pre==None:
            self.head=current.getNext()
        else:
            pre.setNext(current.getNext())

myList=UnorderedList()
myList.add(1)
myList.add(2)
myList.add(4)
myList.add(3)
myList.add(12)
myList.add(92)
print(myList.show())
print(myList.search(12))
myList.remove(1)
print(myList.show())