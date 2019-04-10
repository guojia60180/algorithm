#Author guo
# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        num1=''
        num2=''
        while l1:
            num1=num1+str(l1.val)
            l1=l1.next
        while l2:
            num2=num2+str(l2.val)
            l2=l2.next
        add=str(int(num1)+int(num2))
        head=ListNode(add[0])
        res=head
        for i in range(1,len(add)):
            node=ListNode(add[i])
            head.next=node
            head=head.next
        return res

    def addTwoNumbers2(self,l1,l2):
        stack1=[]
        stack2=[]
        while l1:
            stack1.append(l1.val)
            l1=l1.next
        while l2:
            stack2.append(l2.val)
            l2=l2.next

        answer=None
        carry=0
        while stack2 and stack1:
            add=stack1.pop()+stack2.pop()+carry
            carry=1 if add>=10 else 0
            temp=answer
            answer=ListNode(add%10)
            answer.next=temp

        l=stack1 if stack1 else stack2
        while l:
            add=l.pop()+carry
            carry=1 if add>=10 else 0
            temp=answer
            answer=ListNode(add%10)
            answer.next=temp

        if carry:
            temp=answer
            answer=ListNode(1)
            answer.next=temp

        return answer