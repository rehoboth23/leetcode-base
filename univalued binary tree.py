# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        """

        :param root: root tree
        :return: if tree is univalued i.e. all nodes have the same value
        """
        if not (root.left or root.right):
            # returns True for root with no children
            return True

        # presets lval and rval to self val as if they don't exist then they may as well be equal to node's val
        lstate = True
        lval = root.val
        rstate = True
        rval = root.val
        if root.left:
            lstate = self.isUnivalTree(root.left)
            lval = root.left.val
        if root.right:
            rstate = self.isUnivalTree(root.right)
            rval = root.right.val
        if not (lstate and rstate):
            # returns false if either left branch or right branch return false
            return False
        else:
            # if both branches are true return if val is equal to both left and right val
            return root.val == lval and root.val == rval
