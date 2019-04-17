#Author guo
class Solution:
    def constructArray(self, n, k):
        #给出一个排列，使其相邻元素的差的绝对值有指定的k种
        a=list(range(1,n+1))
        for i in range(1,k):
            a[i:]=a[:i-1:-1]#翻转操作
        return a

    '''
    从生成的元素，相邻的绝对值差为1
    把后面的翻转一次，使1 10相邻 就有了2种
    然后翻转9到2 就有三种
    每翻转一次，就多一次
    '''

    def constructArray2(self, n, k):
        res=[]
        l,r=1,n
        while l<=r:
            if k>1:
                if k%2==1:
                    res.append(l)
                    l+=1
                else:
                    res.append(r)
                    r-=1
                k-=1
            else:
                res.append(l)
                l+=1
        return res

    '''
    每次选择一个数字放在结果数组里，选取方式从两头向中间取
    每次取一个数字就会产生一个不同的差值，k-1
    当k还剩1时，后面的数字从小到大排列，后面的数字差值是1
    '''
