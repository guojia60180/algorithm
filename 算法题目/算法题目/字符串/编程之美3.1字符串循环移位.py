#Author guo
#s1 = AABCD, s2 = CDAA
# Return : true

'''
给定两个字符串s1和s2，要求判定s2是否能够被s1做循环移位得到的字符串包含

s1进行循环移位的结果是s1s1的子字符串，因此只要判定s2是否是s1s1的字符串
'''
s1='AABCD'
s2='CDAA'
s=s1+s1
if s2 in s1:
    print(True)
else:
    print(False)

########################################################################
##                      编程之美3.1 字符串移位的包含问题                  ##
########################################################################
# 字符串'ABCD'循环移动之后包含'DAB'
# 此题的核心是'ABCD'=>'ABCDABCD'其中的3字符字串就是可以得到的所有3字符字串

#类似题目，移动字符串ABCD12向右移动两位,12ABCD,但是最多使用两个变量空间
# 一个做法同上拼接后切割,但是这样需要多余的空间,不符合要求，这种做法实际就是字符串复制
# 算法1:  算法 2.17 用三次旋转实现，线性时间，但是只使用一个旋转用的变量

#算法2:双指针移动法：对于一个字符串或者数组123456789,要向左移动m位,那么可以用两个指针
# p1=0;p2=p1+m;p1,p2一边向前移动一边交换p1,p2，对于末尾的递归实现上述步骤可以实现移动
# 如1234，m=2,=>3214=>3412 完成。12345,m=2 32145=》34125=》34521=》34512

#stl里的rotate算法，用到了gcd的原理
def leftRotate(astr,n,m,head,tail):

    #n 待处理部分的字符串长度，m：待处理部分的旋转长度
    #head：待处理部分的头指针，tail：待处理部分的尾指针

    # 返回条件
    if head == tail or m <= 0:
        return astr
    p1=head
    p2=head+m

    #1、左旋：对于字符串abc def ghi gk，
    #将abc右移到def ghi gk后面，此时n = 11，m = 3，m’ = n % m = 2;
    #abc def ghi gk -> def ghi abc gk

    k = (n - m) - n % m   #p1，p2移动距离，向右移六步

        #---------------------
        #解释下上面的k = (n - m) - n % m的由来：
        #以p2为移动的参照系：
        #n-m 是开始时p2到末尾的长度，n%m是尾巴长度
        #(n-m)-n%m就是p2移动的距离
        #比如 abc def efg hi
        #开始时p2->d,那么n-m 为def efg hi的长度8，
        #n%m 为尾巴hi的长度2，
        #因为我知道abc要移动到hi的前面，所以移动长度是
        #(n-m)-n%m = 8-2 = 6。
        #*/
    i=0
    while i<k:
        astr[p1],astr[p2]=astr[p2],astr[p1]
        i+=1
        p1+=1
        p2+=1
        # print (i,p1,p2)
    print (astr,n-k,n,m,p1,p2,head,tail)
    return rightRotate(astr, n - k, n % m, p1, tail)  #结束左旋，下面，进入右旋

def rightRotate(astr,n,m,head,tail):
    if head == tail or m <= 0:
        return astr

    #2、右旋：问题变成gk左移到abc前面，此时n = m’ + m = 5，m = 2，m’ = n % m 1;
    #abc gk -> a gk bc

    p1 = tail
    p2 = tail - m

    #p1，p2移动距离，向左移俩步
    k = (n - m) - n % m;
    i=0
    while i<k:
        astr[p1],astr[p2]=astr[p2],astr[p1]
        i+=1
        p1-=1
        p2-=1
    print (astr,n-k,n,m,p1,p2,head,tail)
    return leftRotate(astr, n - k, n % m, head, p1)#再次进入上面的左旋部分，
    #3、左旋：问题变成a右移到gk后面，此时n = m’ + m = 3，m = 1，m’ = n % m = 0;
    #a gk bc-> gk a bc。 由于此刻，n % m = 0，满足结束条件，返回结果。

'''
   1、对于正整数m、n互为质数的情况，通过以下过程得到序列的满足上面的要求：
 for i = 0: n-1
      k = i * m % n;
 end

    举个例子来说明一下，例如对于m=3,n=4的情况，
        1、我们得到的序列：即通过上述式子求出来的k序列，是0, 3, 2, 1。
        2、然后，你只要只需按这个顺序赋值一遍就达到左旋3的目的了：
    ch[0]->temp, ch[3]->ch[0], ch[2]->ch[3], ch[1]->ch[2], temp->ch[1]; （*）

    ok，这是不是就是按上面（*）式子的顺序所依次赋值的序列阿?哈哈，很巧妙吧。当然，以上只是特例，作为一个循环链，相当于rotate算法的一次内循环。

2、对于正整数m、n不是互为质数的情况（因为不可能所有的m，n都是互质整数对），那么我们把它分成一个个互不影响的循环链，
所有序号为 (j + i * m) % n（j为0到gcd(n, m)-1之间的某一整数，i = 0:n-1）会构成一个循环链，一共有gcd(n, m)个循环链，对每个循环链分别进行一次内循环就行了。

    综合上述两种情况，可简单编写代码如下：

//④ 所有序号为 (j+i *m) % n (j 表示每个循环链起始位置，i 为计数变量，m表示左旋转位数，n表示字符串长度)，
//会构成一个循环链（共有gcd(n,m)个，gcd为n、m的最大公约数），

//每个循环链上的元素只要移动一个位置即可，最后整个过程总共交换了n次
//（每一次循环链，是交换n/gcd(n,m)次，共有gcd(n,m)个循环链，所以，总共交换n次）。

void rotate(string &str, int m)
{
    int lenOfStr = str.length();
    int numOfGroup = gcd(lenOfStr, m);
    int elemInSub = lenOfStr / numOfGroup;

    for(int j = 0; j < numOfGroup; j++)
        //对应上面的文字描述，外循环次数j为循环链的个数，即gcd(n, m)个循环链
    {
        char tmp = str[j];

        for (int i = 0; i < elemInSub - 1; i++)
            //内循环次数i为，每个循环链上的元素个数，n/gcd(m,n)次
            str[(j + i * m) % lenOfStr] = str[(j + (i + 1) * m) % lenOfStr];
        str[(j + i * m) % lenOfStr] = tmp;
    }
}
'''


## 根据上面的描述，写出算法3
def moveGcd(astr,m):
    lenS=len(astr)
    numOfGroup=gcd(lenS,m)
    elemInSub=lenS//numOfGroup

    for j in range(numOfGroup):

        #对应上面的文字描述，外循环次数j为循环链的个数，即gcd(n, m)个循环链
        temp=''
        for  i in range(elemInSub - 1):
            #内循环次数i为，每个循环链上的元素个数，n/gcd(m,n)次
            astr[(j + i * m) % lenS] = astr[(j + (i + 1) * m) % lenS]
        astr[(j + i * m) % lenS] = temp

    return  astr


def test3_1():
    astr='helloworld'
    print (leftRotate(list(astr),10,3,0,9))
    print (moveGcd(list(astr),3))