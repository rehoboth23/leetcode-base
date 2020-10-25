# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:

        def checkSubnodes(root, target):
            if (not root and target) or (root and not target):
                return False
            elif not root and not target:
                return True
            elif root.val != target.val:
                return False
            else:
                return checkSubnodes(root.left, target.left) and checkSubnodes(root.right, target.right)

        def findNode(root, target):
            if not root:
                return False
            check = False
            if root.val == target.val:
                check = checkSubnodes(root, target)

            return check or findNode(root.right, target) or findNode(root.left, target)

        return findNode(s, t)
