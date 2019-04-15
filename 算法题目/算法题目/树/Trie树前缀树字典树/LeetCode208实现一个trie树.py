#Author guo
#trie树，前缀树或字典树，用于判断字符串是否存在或者具有某种字符串前缀
'''
归纳字典树的性质
1.根结点不包含字符，除根结点以外的每一个子节点包含一个字符
2.从根节点到某一个节点，路径上经过的字符连接起来，为该节点对应的字符串
3.通常在实现的时候，会在节点结构中设置一个标志，用来标记该节点处是否构成一个单词

每个节点的子孩子都是一个字典，根据字典查找下一个位置的节点
'''
import collections
class Node:
    def __init__(self):
        self.children=collections.defaultdict(Node)
        self.isword=False
class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root=Node()
    def insert(self, word):
        """
        Inserts a word into the trie.
        """
        current=self.root
        for w in word:
            current=current.children[w]
        current.isword=True
    def search(self, word) :
        """
        Returns if the word is in the trie.
        """
        current=self.root
        for w in word:
            current=current.children.get(w)
            if current==None:
                return False
        return current.isword
    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        current=self.root
        for w in prefix:
            current=current.children.get(w)
            if current==None:
                return False
        return True


        # Your Trie object will be instantiated and called as such:
        # obj = Trie()
        # obj.insert(word)
        # param_2 = obj.search(word)
        # param_3 = obj.startsWith(prefix)