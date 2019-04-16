#Author guo
#将字符串向右循环移动k位
'''
s = "abcd123" k = 3
Return "123abcd"
'''
def leftloop(s, k):
    """
    字符串循环左移
    :param s: 字符串数组
    :param k: 字符串循环左移k位
    :return:
    """
    if s is None:
        return
    n = len(s)
    if n < k:
        return
    reverse(s, 0, k - 1)
    reverse(s, k, n - 1)
    reverse(s, 0, n - 1)


def reverse(s, i, j):
    """
    翻转
    :param s: 字符串数组
    :param i: 翻转开始位置
    :param j: 翻转结束位置
    """
    if s is None or i < 0 or j < 0 or i >= j or len(s) < j + 1:
        return
    while i < j:
        temp = s[i]
        s[i] = s[j]
        s[j] = temp
        i += 1
        j -= 1


if __name__ == '__main__':
    s = "abcdef"
    print(s)
    li = list(s)
    leftloop(li, 2)
    print(''.join(li))
