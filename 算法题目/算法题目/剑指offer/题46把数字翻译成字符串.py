#Author guo
def trans_num_to_str(num):
    if num<0:
        return 0
    #if num==1:
    #    return 'b'
    string=str(num)
    if len(string)==1:
        return 1
    if len(string)==2:
        if int(string)<=25:
            return 3
        else:
            return 2

    #从后到前的遍历
    f1=0
    f2=1
    g=0
    for i in range(len(string)-2,-1,-1):
        if int(string[i]+string[i+1])<=25:
            g=1
        else:
            g=0
        f2,f1=f2+g*f1,f2

    return f2
print(trans_num_to_str(26))