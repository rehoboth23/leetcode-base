# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        rem = 0
        res = None

        while l1 or l2:

            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            s = a + b + rem
            rem = 0
            if s < 10:
                nextNode = ListNode(s)
            else:
                r = s - 10
                nextNode = ListNode(r)
                rem = 1
            if res == None:
                res = nextNode
            else:
                self.insertNode(res, nextNode)

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if rem == 1:
            nextNode = ListNode(1)
            self.insertNode(res, nextNode)
        return res

    def insertNode(self, head: ListNode, node: ListNode):
        if head.next == None:
            head.next = node
            return
        else:
            self.insertNode(head.next, node)
