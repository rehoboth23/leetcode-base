# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        """

        :param head: first node of list
        :param k: number of rotate
        :return: rotated list
        working theory is to get the last item in the list and set its predecessors next to None
        add the temps Item's next as head, then set head to temp,
        do this as many rotations as necessary

        optimization is to use modulus to reduce the number of rotations needed as every N rotations assuming N to be
        length of the list, the list resets. so k mod n will give the number of viable rotations
        """
        if not head:
            # return list if empty
            return head

        self.temp = None

        def findLast(node, count):

            # if last node return none  except when head i.e count == 0 then break out because length of list = 1
            # set node's next to return value
            if not node.next:
                if count == 0:
                    return
                self.temp = ListNode(node.val)
                return None
            res = findLast(node.next, count + 1)
            node.next = res
            return node

        # count counts the nodes in a list
        def count(node):
            if not node:
                return 0
            return 1 + count(node.next)

        # rotates 1 time for k rounds
        for i in range(k % count(head)):
            findLast(head, 0)
            if self.temp:
                self.temp.next = head
                head = self.temp

        return head
