# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        """

        :param head: first node in list
        :return: altered list
        working theory, uses the sum and rem method
        the find next works to find the next element at from the back of the list to add to
        when there is no remainder return the head,
        when the current value is the head and the first escape was not used, there must be a remainder
        then create a new node, set it's next as head then return the node
        """

        curr: ListNode = self.findNext(head)
        rem: int = 1
        while True:
            s = curr.val + rem
            if s >= 10:
                r = s - 10
                curr.val = r
            else:
                rem = 0
                curr.val = s
                break
            if curr == head:
                newHead = ListNode(1, head)
                return newHead
            curr = self.findNext(head, curr)


    def findNext(self, node: ListNode, stop=None):
        if node.next == stop:
            return node
        else:
            return self.findNext(node.next, stop)
