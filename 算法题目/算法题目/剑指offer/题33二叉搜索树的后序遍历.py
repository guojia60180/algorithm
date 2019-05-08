#Author guo
# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence or len(sequence) == 0:
            return False

        root = sequence[-1]

        # 找index，index前的数都小于root，index后的数都大于root
        if min(sequence) > root or max(sequence) < root:
            return True

        index = 0

        for i in range(len(sequence) - 1):
            index = i
            if sequence[i] > root:
                break

        for j in range(index + 1, len(sequence) - 1):
            if sequence[j] < root:
                return False

        left = True
        if index > 0:
            left = self.VerifySquenceOfBST(sequence[:index])#左节点

        right = True
        if index < len(sequence) - 1:#小于边界值
            right = self.VerifySquenceOfBST(sequence[index:len(sequence) - 1])#右节点，分别进行计算
            #递归的完成

        return left and right

