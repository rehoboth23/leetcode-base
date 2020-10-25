# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    """
    uses an internal helper method insert to insert the elementf os an linked list into another linked list
    """
    def mergeKLists(self, lists: [ListNode]) -> ListNode:
        if not lists:
            return None
        root = lists[0]

        def insert(node, llist):
            if not llist:
                return node
            elif not node:
                return llist
            elif llist.val <= node.val:
                temp = llist.next
                llist.next = insert(node, temp)
                return llist
            else:
                node.next = insert(node.next, llist)
                return node

        for i in range(1, len(lists)):
            root = insert(root, lists[i])
        return root
