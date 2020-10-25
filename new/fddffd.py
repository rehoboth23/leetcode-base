class ListNode(object):
    def __init__(self, x, n=None):
        self.val = x
        self.next = n

    def __str__(self):
        cur = self
        result = ""
        while cur:
            result += str(cur.val) + " -> "
            cur = cur.next
        return result + "None"



class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        def insert(curr, node):
            if not curr:
                return node
            else:
                curr.next = insert(curr.next, node)
                return curr

        def findLast(node):
            if not node: return (None, None)
            if not node.next:
                return (node, None)
            else:
                res: ListNode = findLast(node.next)
                node.next = res[1]
                return (res[0], node)

        curr: ListNode = ListNode(float('inf'))
        while head:
            temp, head = findLast(head)
            insert(curr, temp)

        return curr.next

    def reverseList2(self, head):
        self.res = None

        def reverse(node, prev):
            if not node:
                res = prev
            if not node.next:
                self.res = node
                if prev:
                    self.res.next = ListNode(prev.val, None)
                else:
                    self.res.next = None
                return self.res.next
            else:
                newnode = node.next
                n = reverse(newnode, node)
                if prev:
                    n.next = ListNode(prev.val, None)
                else:
                    n.next = None
                return n.next

        reverse(head, None)
        return self.res