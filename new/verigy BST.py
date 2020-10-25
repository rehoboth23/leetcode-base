# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    BY bounds, you can dictate the allowed range for the value of every node
    """
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(node: TreeNode, lowerlimit, upperlimit):
            if not node:
                return True
            val = node.val
            if val <= lowerlimit or val >= upperlimit: return False
            if not helper(node.right, val, upperlimit): return False
            if not helper(node.left, lowerlimit, val): return False
            return True

        return helper(root, -float('inf'), float('inf'))

