#Author guo
#三种方式实现
class AnagramDetection:
    #先对两个字符串list
    #对字符串对应的两个list排序
    #依次比较两个list
    def anagramDection1(self,s1,s2):
        list1=list(s1)
        list2=list(s2)

        list1=sorted(list1)
        list2=sorted(list2)

        pos=0
        match=True

        while pos<len(s1) and match==True:
            if list1[pos]==list2[pos]:
                pos+=1

            else:
                match=False

        return match

    #采用标准库中的Counter计数器对字符串进行统计
    #字典没有顺序，因此可以比较两个字典是否相同
    def anagramDection2(self,s1,s2):
        import collections

        dic1=collections.Counter(s1)
        dic2=collections.Counter(s2)
        # print(dic1)
        # print(dic2)

        return dic1==dic2
    #生成26个字母的list
    #计算没每个字母出现的次数并存入相应的list中
    #比较两个list是否相同
    def anagramDetection3(self,s1,s2):
        c1=[0]*26
        c2=[0]*26

        for i in range(len(s1)):
            pos=ord(s1[i])-ord('a')
            c1[pos]=c1[pos]+1

        for i in range(len(s2)):
            pos=ord(s2[i])-ord('a')
            c2[pos]=c2[pos]+1


        j=0
        match=True
        while j<26 and match:
            if c1[j]==c2[j]:
                j=j+1
            else:
                match=False

        return match

    def anagramDetection4(self,s1,s2):
        #两个字符串list化
        #生成两个set
        #比较两个set，如果不相等直接返回False
        #相等比较set字符在对应list中的个数
        list1=list(s1)
        list2=list(s2)
        set1=set(list1)
        set2=set(list2)

        if set1!=set2:
            return False
        else:
            for ch in set1:
                if list1.count(ch)!=list2.count(ch):
                    return False
            return True

s1 = 'abcde'
s2 = 'acbde'
test = AnagramDetection()
test.anagramDection1(s1,s2)
test.anagramDection2(s1,s2)
test.anagramDetection3(s1,s2)
test.anagramDetection4(s1,s2)
#print(test.anagramDection1(s1,s2))