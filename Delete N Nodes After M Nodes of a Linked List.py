# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteNodes(head: ListNode, m: int, n: int) -> ListNode:
    """
    :param head: root node
    :param m: m nodes to not delete from
    :param n: n nodes to delete after m nodes
    :return:  altered list
    """
    curr = ListNode(0)
    curr.next = head
    c_n, c_m = n, m

    while curr:
        if c_m > 0:
            curr = curr.next
            c_m -= 1
            if not curr:
                break
        if c_m == 0 and c_n > 0:
            if curr.next:
                curr.next = curr.next.next
            c_n -= 1
        if c_m == 0 and c_n == 0:
            c_m, c_n = m, n
    return head

