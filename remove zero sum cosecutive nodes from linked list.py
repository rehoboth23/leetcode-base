# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        """
        :param head: first element of list
        :return: linked list with zero sums removed
        working theory: make the array into a list, then check every incrementing sublist of the array for a zero sum,
        remove all values involved in the zero sum
        if a zero sum wa found check sub array again
        else increment pointer
        parse array back into a linked list at the end
        """
        arr: [int] = []
        self.makeArray(arr, head)

        i = 0

        while i < len(arr):
            stop = self.checkSubArrays(i, arr)
            if stop == -1:
                i += 1
            continue
        linkedList = self.makeList(arr[::-1])
        return linkedList

    def makeArray(self, arr: [int], node: ListNode):
        if node == None:
            return
        else:
            arr.append(node.val)
            self.makeArray(arr, node.next)

    def checkSubArrays(self, start, arr):
        a_sum = None
        stop = -1
        for i in range(start, len(arr)):
            if not a_sum:
                a_sum = arr[i]
            else:
                a_sum += arr[i]
            if a_sum == 0:
                stop = i + 1
                break
        for i in range(stop - start):
            arr.pop(start)
        return stop

    def makeList(self, arr: [int]):
        if len(arr) == 0:
            return None
        newNode = ListNode(arr.pop())
        newNode.next = self.makeList(arr)
        return newNode


