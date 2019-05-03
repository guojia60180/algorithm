#Author guo
#实现基数排序，高位优先和低位优先

#最低位优先

def radixSort(list):
    if len(list)==0:
        return
    if len(list)==1:
        return list

    templist=list
    maxNum=max(list)
    radix=10
    while maxNum*10>radix:
        newArr=[[], [], [], [], [], [], [], [], [], []]
        for n1 in templist:
            testnum=n1%radix
            testnum=testnum//(radix/10)
            for n2 in range(10):
                if testnum==n2:
                    newArr[n2].append(n1)


        templist=[]
        for i in range(len(newArr)):
            for j in range(len(newArr[i])):
                templist.append(newArr[i][j])
        radix*=10

    return templist

print(radixSort([10, 12, 24, 23, 13, 52, 15, 158, 74, 32, 254, 201, 30, 19]))