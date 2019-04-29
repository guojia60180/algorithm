#Author guo
class TreeNode:
    def __init__(self,key,val,left=None,right=None,parent=None):
        self.key=key
        self.payload=val
        self.leftchild=left
        self.rightchild=right
        self.parent=parent

    def hasLeftchild(self):
        return self.leftchild

    def hasRightchild(self):
        return self.rightchild

    def isleftchild(self):
        return self.parent and self.parent.leftchild==self

    def isrightchild(self):
        return self.parent and self.parent.rightchild==self

    def isroot(self):
        return not self.parent

    def isleaf(self):
        return not(self.rightchild or self.leftchild)

    def hasAnychildren(self):
        return self.rightchild or self.leftchild

    def hasBothcildren(self):
        return self.rightchild and self.leftchild

    def replaceNodeData(self,key,value,lc,rc):
        self.key=key
        self.payload=value
        self.leftchild=lc
        self.rightchild=rc
        if self.hasLeftchild():
            self.leftchild.parent=self

        if self.hasRightchild():
            self.rightchild.parent=self

class BinarySearchTree:
    def __init__(self):
        self.root=None
        self.size=0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def put(self,key,val):
        if self.root:
            self._put(key,val,self.root)
        else:
            self.root=TreeNode(key,val)
        self.size=self.size+1

    def _put(self,key,val,currentNode):
        if key<currentNode.key:
            if currentNode.hasLeftchild():
                self._put(key,val,currentNode.leftchild)
            else:
                currentNode.leftchild=TreeNode(key,val,parent=currentNode)
                self.updateBalance(currentNode.leftchild)
        else:
            if currentNode.hasRightchild():
                self._put(key,val,currentNode.rightchild)
            else:
                currentNode.rightchild=TreeNode(key,val,parent=currentNode)
                self.updateBalance(currentNode.rightchild)

    def updateBalance(self,node):
        if node.balanceFactor>1 or node.balanceFactor<-1:
            self.rebanlace(node)
            return

        if node.parent!=None:
            if node.isleftchild():
                node.parent.balanceFactor+=1
            elif node.isrightchild():
                node.parent.balanceFactor-=1

            if node.parent.balanceFactor!=0:
                self.updateBalance(node.parent)

    def rotateleft(self,rotRoot):
        newRoot=rotRoot.rightchild
        rotRoot.rightchild=newRoot.leftchild
        if newRoot.leftchild!=None:
            newRoot.leftchild.parent=rotRoot

        newRoot.parent=rotRoot.parent
        if rotRoot.isroot():
            self.root=newRoot

        else:
            if rotRoot.isleftchild():
                rotRoot.parent.leftchild=newRoot
            else:
                rotRoot.parent.rightchild=newRoot

        newRoot.leftchild=rotRoot

        rotRoot.parent=newRoot
        rotRoot.balanceFactor=rotRoot.balanceFactor + 1 - min(newRoot.balanceFactor, 0)
        newRoot.balanceFactor = newRoot.balanceFactor + 1 - max(newRoot.balanceFactor, 0)

    def rotateright(self, rotRoot):
        newRoot = rotRoot.leftchild
        rotRoot.leftchild = newRoot.rightchild
        if newRoot.rightchild != None:
            newRoot.rightchild.parent = rotRoot

        newRoot.parent = rotRoot.parent
        if rotRoot.isroot():
            self.root = newRoot

        else:
            if rotRoot.isrightchild():
                rotRoot.parent.rightchild = newRoot
            else:
                rotRoot.parent.leftchild = newRoot

        newRoot.rightchild = rotRoot

        rotRoot.parent = newRoot
        rotRoot.balanceFactor = rotRoot.balanceFactor + 1 - min(newRoot.balanceFactor, 0)
        newRoot.balanceFactor = newRoot.balanceFactor + 1 - max(newRoot.balanceFactor, 0)

    def rebalance(self,node):
        if node.balanceFactor<0:
            if node.rightchild.balanceFactor>0:
                self.rotateright(node.rightchild)
                self.rotateleft(node)

            else:
                self.rotateleft(node)

        elif node.balanceFactor>0:
            if node.leftchild.banlanceFactor<0:
                self.rotateleft(node.leftchild)
                self.rotateright(node)

            else:
                self.rotateright(node)

    def __setitem__(self, k, v):
        self.put(k,v)

    def get(self,key):
        if self.root:
            res=self._get(key,self.root)
            if res:
                return res.payload

            else:
                return None
        else:
            return None

    def _get(self,key,currentNode):
        if not currentNode:
            return None
        elif currentNode.key==key:
            return currentNode
        elif key<currentNode.key:
            return self._get(key,currentNode)
        else:
            return self._get(key,currentNode)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        if self._get(key,self.root):
            return True
        else:
            return False

    def delete(self,key):
        if self.size>1:
            nodetoremove=self._get(key,self.root)
            if nodetoremove:
                self.remove(nodetoremove)
                self.size-=1

            else:
                raise KeyError('Error')

        elif self.size==1 and self.root.key==key:
            self.root=None
            self.size=self.size-1

        else:
            raise KeyError('Error.0')

    def __delitem__(self, key):
        self.delete(key)

    def spliceOut(self):
        if self.isleaf():
            if self.isleftchild():
                self.parent.leftchild=None

            else:
                self.parent.rightchild=None
        elif self.hasAnychildren():
            if self.hasLeftchild():
                if self.islftchild():
                    self.parent.leftchild=self.leftchild

                else:
                    self.parent.rightchild=self.leftchild

            else:
                if self.islftchild():
                    self.parent.leftchild = self.rightchild

                else:
                    self.parent.rightchild = self.rightchild
                self.rightchild.parent=self.parent

    def findSuccessor(self):
        succ=None
        if self.hasRightchild():
            succ=self.rightchild.findmin()
        else:
            if self.parent:
                if self.isleftchild():
                    succ=self.parent

                else:
                    self.parent.rightchild=None
                    succ=self.parent.findSuccessor()
                    self.parent.rightchild=self

        return succ

    def findmin(self):
        current=self
        while current.hasLeftchild():
            current=current.leftchild

        return current

    def remove(self,currentNode):
        if currentNode.isleaf():
            if currentNode==currentNode.parent.leftchild:
                currentNode.parent.leftchild=None
            else:
                currentNode.parent.rightchild=None

        elif currentNode.hasBothchildren():
            succ=currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.key=succ.key
            currentNode.payload=succ.payload

        else:
            if currentNode.hasLeftchild():
                if currentNode.isleftchild():
                    currentNode.leftchild.parent=currentNode.parent
                    currentNode.parent.leftchild=currentNode.leftchild

                elif currentNode.isrightchild():
                    currentNode.leftchild.parent=currentNode.parent
                    currentNode.parent.rightchild=currentNode.leftchild

                else:
                    currentNode.replaceNodeData(
                        currentNode.leftchild.key,currentNode.leftchild.payload,
                        currentNode.leftchild.leftchild,currentNode.leftchild.rightchild
                    )

            else:
                if currentNode.isleftchild():
                    currentNode.rightchild.parent = currentNode.parent
                    currentNode.parent.leftchild = currentNode.rightchild

                elif currentNode.isleftchild():
                    currentNode.roghtchild.parent = currentNode.parent
                    currentNode.parent.leftchild = currentNode.rightchild

                else:
                    currentNode.replaceNodeData(
                        currentNode.rightchild.key, currentNode.rightchild.payload,
                        currentNode.rightchild.leftchild, currentNode.rightchild.rightchild
                    )

mytree=BinarySearchTree()
mytree[3]="red"
mytree[4]="blue"
mytree[6]="yellow"
mytree[2]="at"

print(mytree[6])
print(mytree[2])