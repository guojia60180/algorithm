#Author guo
#输入hello 错误输入hellu 找出出错的字母
#对词典中每个次，逐次逐字母拓展Trie树
#单词完结处结点用END符号标识

END='$'

def make_trie(words):
    trie={}
    for word in words:
        t=trie
        for c in word:
            if c not in t:
                t[c]={}
            t=t[c]
        t[END]={}

    return trie

#容错查找
#实质对trie树深度优先搜索，每一步加深时就消耗目标词的一个字母
#当搜索到某个结点时
#分为不消耗容错数和消耗容错数的情形，继续搜索直到目标词为空
#搜索过程中，用path记录搜索路径，路径即为一个词典中存在的词
#纠错的参考
#最终结果即为诸多搜索停止位置的结点路径的并集

def check_fuzzy(trie,word,path='',tol=1):
    if word=='':
        return [path] if END in trie else []

    else:
        p0=[]
        if word[0] in trie:
            p0=check_fuzzy(trie[word[0]],word[1:],path+word[0],tol)
        p1=[]
        if tol>0:
            for k in trie:
                if k!=word[0]:
                    p1.extend(check_fuzzy(trie[k],word[1:],path+k,tol-1))
        return p0+p1


words=['hello','kha','dome']
t=make_trie(words)
print(t)
print(check_fuzzy(t,'hellu'))
print(check_fuzzy(t,'healu',tol=2))