# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """

        :param head: first node in list
        :return: altered list
        working theory: as the list is sorted, if node.next and node.next.val equal to node.val, then set node.next
        to node.next.next. if a duplicate is removed, passing hte node into the recursion simulates a while loop
        if no duplicate is seen then advance to the next node
        """
        self.removeDuplicate(head)
        return head

    def removeDuplicate(self, node: ListNode):

        if not node or node.next == None:
            return
        elif node.val == node.next.val:
            node.next = node.next.next
            self.removeDuplicate(node)
        else:
            self.removeDuplicate(node.next)