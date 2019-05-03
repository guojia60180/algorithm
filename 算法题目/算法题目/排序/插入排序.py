#Author guo
def insertionSort(list):
    for key,item in enumerate(list):
        index=key
        while index>0 and list[index-1]>item:
            list[index]=list[index-1]
            index-=1
        list[index]=item

    return list

def insertionSort2(list):
    for index in range(1,len(list)):
        currentvalue=list[index]
        position=index

        while position>0 and list[position-1]>currentvalue:
            list[position]=list[position-1]
            position-=1
        list[position]=currentvalue

    return list
list = [54,26,93,17,77,31,44,55,20]
print(insertionSort(list))