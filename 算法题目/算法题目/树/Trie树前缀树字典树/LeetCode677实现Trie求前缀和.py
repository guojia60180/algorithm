#Author guo
'''
使用前缀树，在每个经过的节点都保存了以此节点为前缀的字符串
的值的和

求和过程转换为-》找出相应的前缀对应的和即可
如果相同字符串插入操作是进行覆盖的
'''
import collections
class Node:
    def __init__(self,count=0):
        self.children=collections.defaultdict(Node)
        self.count=count
class MapSum:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root=Node()
        self.keys={}


    def insert(self, key, val):
        curr=self.root
        delta=val-self.keys.get(key,0)
        #更新保存键值对的key
        self.keys[key]=val
        curr=self.root
        #更新节点的count值
        curr.count+=delta
        for char in key:
            curr=curr.children[char]
            curr.count+=delta


    def sum(self, prefix):
        curr=self.root
        for char in prefix:
            if char not in curr.children:
                return 0
            curr=curr.children[char]
        return curr.count
    # Your MapSum object will be instantiated and called as such:
    # obj = MapSum()
    # obj.insert(key,val)
    # param_2 = obj.sum(prefix)