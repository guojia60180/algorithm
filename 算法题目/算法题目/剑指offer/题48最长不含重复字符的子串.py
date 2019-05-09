#Author guo
def longestSubstringWithoutDup(string):
    start=0
    maxlen=0
    usedChar={}
    for i in range(len(string)):
        if string[i] in usedChar and start<=usedChar[string[i]]:#如果出现在用过的字典中
            #而且开始点小于string[i]的位置
            start=usedChar[string[i]]+1
            #start指针变为出现的节点处+1
        else:
            maxlen=max(maxlen,i-start+1)#没有出现，maxlen+=1
        usedChar[string[i]]=i

    return maxlen