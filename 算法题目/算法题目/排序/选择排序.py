#Author guo
def selectionSort(list):
    for i in range(len(list)-1):
        min=i
        for j in range(i+1,len(list)):
            if list[j]<list[min]:
                min=j
        list[i],list[min]=list[min],list[i]

    return list
list = [54,26,93,17,77,31,44,55,20]
print(selectionSort(list))
