# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        elif root.val < val:
            res = TreeNode(val, root)
            return res
        else:
            root.right = self.insertIntoMaxTree(root.right, val)
            return root
