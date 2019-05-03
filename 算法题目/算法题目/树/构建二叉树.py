#Author guo
class BinaryTree:
    def __init__(self,rootObj):
        self.key=rootObj
        self.leftchild=None
        self.rightchild=None

    def insertleft(self,newNode):
        if self.leftchild==None:
            self.leftchild=BinaryTree(newNode)

        else:
            t=BinaryTree(newNode)
            t.leftchild=self.leftchild
            self.leftchild=t

    def insertright(self,newNode):
        if self.rightchild == None:
            self.rightchild = BinaryTree(newNode)

        else:
            t = BinaryTree(newNode)
            t.rightchild = self.rightchild
            self.rightchild = t

    def getrightchild(self):
        return self.rightchild

    def getleftchild(self):
        return self.leftchild

    def setrootval(self,obj):
        self.key=obj

    def getrootval(self):
        return self.key


    #前序遍历
    def preorder(self):
        print(self.key)
        if self.leftchild:
            self.leftchild.preorder()
        if self.rightchild:
            self.rightchild.preorder()

r = BinaryTree('a')
print(r.getrootval())
print(r.getleftchild())
r.insertleft('b')
print(r.getleftchild())
print(r.getleftchild().getrootval())
r.insertright('c')
print(r.getrightchild())
print(r.getrightchild().getrootval())
r.getrightchild().setrootval('hello')
print(r.getrightchild().getrootval())