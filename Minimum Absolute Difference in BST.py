# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        """
        :param root: root tree node
        :return: min absolute difference of any two nodes in the tree
        """
        val = self.getdifference(root, set())
        return val

    def getdifference(self, node, seen):
        """

        :param node: node being considered
        :param seen: set of seen values
        :return: minimum difference achieved
        working theory:
        the diff for a root node will always be infinity
        if the tree has a left, the left is calculated as the minimum is found between diff a left diff using recursion
        if not left diff if just preset to left
        the same is done for the right
        the minimum between the right and left is returned
        calMin is a function which calculates the minimum difference bwteen a value and any value in a collection
        """
        left = 0
        right = 0
        diff = self.calcMin(node.val, seen)

        seen.add(node.val)
        if node.left:
            l_diff = self.getdifference(node.left, seen)
            left = min(l_diff, diff)
        else:
            left = diff
        if node.right:
            r_diff = self.getdifference(node.right, seen)
            right = min(r_diff, diff)
        else:
            right = diff
        return min(right, left)

    def calcMin(self, val, seen):
        minval = float("inf")
        for i in seen:
            minval = min(abs(i - val), minval)
        return minval


class Solution2:

    def minDiffInBST(self, root: TreeNode) -> int:

        def to_array(node, arr):
            if not node:
                return
            else:
                arr.append(node.val)
                to_array(node.left, arr)
                to_array(node.right, arr)

        res_arr = []
        to_array(root, res_arr)
        res_arr.sort()
        max_diff = min(res_arr[x + 1] - res_arr[x] for x in range(len(res_arr) - 1))
        return max_diff




