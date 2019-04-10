#Author guo
#把链表分隔为k部分，每部分长度尽可能相同，排在前面的长度应该大于等于后面的

# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        nodes = []
        counts = 0
        each = root
        while each:
            counts += 1
            each = each.next
        num = counts / k
        rem = counts % k
        for i in range(k):
            head = ListNode(0)
            each = head
            for j in range(num):
                node = ListNode(root.val)
                each.next = node
                each = each.next
                root = root.next
            if rem and root:
                rmnode = ListNode(root.val)
                each.next = rmnode
                if root:
                    root = root.next
                rem -= 1
            nodes.append(head.next)
        return nodes
