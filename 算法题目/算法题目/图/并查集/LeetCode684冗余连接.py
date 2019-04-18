#Author guo
#并查集可以动态的连接两个点，并且可以非常快速的判断两个点是否联通
class Solution:
    def findRedundantConnection(self, edges):
        #给出了一个有环无向图的各个边，找出能去除的边，使这个图不含环
        #这个图的各个节点时1-N，总共有N条边，即只多了一条边

        '''
        告诉一条边，去集合里查找这条边的两个结点分别属于哪个树
         根据是否属于一个树，做后续的判断
         
         
        '''
        tree=[-1]*(len(edges)+1)
        for edge in edges:
            a=self.findRoot(edge[0],tree)
            b=self.findRoot(edge[1],tree)
            if a!=b:
                tree[a]=b
            else:
                return edge


    def findRoot(self,x,tree):
        if tree[x]==-1:
            return x
        else:
            root=self.findRoot(tree[x],tree)
            tree[x]=root
            return root
