#Author guo
def mergeSort(list):
    if len(list)>1:
        mid=len(list)//2
        lefthalf=list[:mid]
        righthalf=list[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                list[k]=lefthalf[i]
                i+=1
            else:
                list[k]=righthalf[j]
                j+=1

            k+=1

        while i<len(lefthalf):
            list[k]=lefthalf[i]
            i+=1
            k+=1

        while j<len(righthalf):
            list[k]=righthalf[j]
            j+=1
            k+=1

list=[54,26,93,17,77,31,44,55,20]
mergeSort(list)
print(list)