#Author guo
def quickSort(list):
    quickSorthelper(list,0,len(list)-1)

def quickSorthelper(list,first,last):
    if first<last:
        spiltPoint=partition(list,first,last)

        quickSorthelper(list,first,spiltPoint-1)
        quickSorthelper(list,spiltPoint+1,last)

def partition(list,first,last):
    pivotvalue=list[first]
    leftmark=first+1
    rightmark=last

    done=False

    while not  done:
        while leftmark<=rightmark and list[leftmark]<=pivotvalue:
            leftmark+=1

        while rightmark>=leftmark and list[rightmark]>=pivotvalue:
            rightmark-=1

        if leftmark>rightmark:
            done=True

        else:
            list[leftmark],list[rightmark]=list[rightmark],list[leftmark]

    list[rightmark],list[leftmark]=list[leftmark],list[rightmark]
    return rightmark

list=[54,26,93,17,77,31,44,55,20]
quickSort(list)

