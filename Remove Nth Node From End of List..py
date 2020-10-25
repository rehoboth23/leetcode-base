# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
        :param head: first node in list
        :param n: nth node to remove
        :return: altered list
        working theory: using a target system, find the element before the parent to the target n times
        if done n times, the last parent to get should be the parent of the nth item to the end
        set its next to it's next's next except when it is the head, set the head to the head's next
        return the head
        """
        curr = None

        for i in range(n):
            curr = self.getPrev(head, curr)

        if curr == head:
            head = curr.next
            return head
        else:
            curr = self.getPrev(head, curr)
            curr.next = curr.next.next
            return head

    def getPrev(self, node: ListNode, target):

        if node.next == target:
            return node
        return self.getPrev(node.next, target)
