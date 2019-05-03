#Author guo
def bubblesort(list):
    for num in range(len(list)-1,0,-1):
        for i in range(num):
            if list[i]>list[i+1]:
                list[i],list[i+1]=list[i+1],list[i]

    return list

list=[54,26,93,17,77,31,44,55,20]

print(bubblesort(list))
#改进，标志位
def bubblesort2(list):
    exchange=True
    passnum=len(list)-1

    while passnum>=1 and exchange:
        exchange=False
        for i in range(passnum):
            if list[i]>list[i+1]:
                list[i],list[i+1]=list[i+1],list[i]
                exchange=True

        passnum-=1
    return list
print(bubblesort2(list))