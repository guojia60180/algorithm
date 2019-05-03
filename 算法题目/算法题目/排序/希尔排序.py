#Author guo

def shellSort(list):
    sublistcount=len(list)//2
    while sublistcount>0:
        for startpos in range(sublistcount):
            gapinsertionsort(list,startpos,sublistcount)
        sublistcount=sublistcount//2

    return list

def gapinsertionsort(list,start,gap):
    for i in range(start+gap,len(list),gap):
        currentValue=list[i]
        position=i

        while position>=gap and list[position-gap]>currentValue:
            list[position]=list[position-gap]
            position=position-gap

        list[position]=currentValue

list = [54,26,93,17,77,31,44,55,20]
print(shellSort(list))