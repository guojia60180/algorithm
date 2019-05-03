#Author guo
def heapSort(list):
    if list==None or len(list)==0:
        return
    length=len(list)
    output=[]

    for i in range(length):
        templen=len(list)
        for j in range(templen//2-1,-1,-1):
            preIndex=j
            preval,heap=list[preIndex],False

            while 2*preIndex<templen-1 and not heap:
                curIndex=2*preIndex+1
                if curIndex<templen-1:
                    if list[curIndex]<list[curIndex+1]:
                        curIndex+=1

                if preval>=list[curIndex]:
                    heap=True
                else:
                    list[preIndex]=list[curIndex]
                    preIndex=curIndex
            list[preIndex]=preval
        output.insert(0,list.pop(0))

    return output

test = [2, 6, 5, 9, 10, 3, 7]
print(heapSort(test))