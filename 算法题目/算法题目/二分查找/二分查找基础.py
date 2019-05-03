#Author guo
#输出，待查找元素的位置
def binarySearch(list,item):
    first=0
    last=len(list)-1

    while first<=last:
        mid=(first+last)//2
        #print(mid)

        if list[mid]>item:
            last=mid-1
        elif list[mid]<item:
            first=mid+1

        else:
            return mid+1

    return -1


test = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(binarySearch(test,13))