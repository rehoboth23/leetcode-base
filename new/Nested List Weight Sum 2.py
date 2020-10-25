# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
   def __init__(self, value=None):
       """
       If value is not specified, initializes an empty list.
       Otherwise initializes a single integer equal to value.
       """

   def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """

   def add(self, elem):
       """
       Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
       :rtype void
       """

   def setInteger(self, value):
       """
       Set this NestedInteger to hold a single integer equal to value.
       :rtype void
       """

   def getInteger(self):
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       :rtype int
       """

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """

class Solution:
    def __init__(self):
        self.max_depth = 0
        self.depth_sum = 0

    def depthSumInverse(self, nestedList: [NestedInteger]) -> int:
        """
        :param nestedList:
        :return: sum by wieghts
        goes down the list to find the max depth
        after finding the max depth, does down the list and sum up the weights
        """
        def max_depth(nest, val):
            if nest.isInteger():
                self.max_depth = max(self.max_depth, val)
                return
            else:
                for renest in nest.getList():
                    max_depth(renest, val + 1)
        for nest in nestedList:
            max_depth(nest, 1)

        def sum_depth(nest, val):
            if nest.isInteger():
                self.depth_sum += nest.getInteger() * val
            else:
                for renest in nest.getList():
                    sum_depth(renest, val - 1)
        for nest in nestedList:
            sum_depth(nest, self.max_depth)

        return self.depth_sum

