# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
   def isInteger(self) -> bool:
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       """

   def getInteger(self) -> int:
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       """

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    """
    flattens recursively
    uses pos = -1 as initial
    """
    def __init__(self, nestedList: [NestedInteger]):
        def flatten(arr):
            for nest in arr:
                if nest.isInteger():
                    self._flatlist.append(nest.getInteger())
                else:
                    flatten(nest.getList())

        self._flatlist = []
        self._pos = -1
        flatten(nestedList)

    def next(self) -> int:
        self._pos += 1
        return self._flatlist[self._pos]

    def hasNext(self) -> bool:
        return self._pos + 1 < len(self._flatlist)

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())