# Definition for a binary tree node.
from typing import Optional, Union, Any


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    This is an implementation of the hubbard deletion. It applies the system of returning the node or replacement node
    on collapsing the recursion stack

    to delete an array first recurse down the tree until the array is found. then get the value of it's smallest
    successor i.e. smallest node in it's right sub-tree. assign that value to the node, then delete that node from it's
    right sub-tree.

    The logic follows that the smallest value node in a BST will have no left child so using the return node system,
    it can be removed as a case with 1 or no children
    """
    def deleteNode(self, root: TreeNode, key: int) -> Optional[TreeNode]:
        if not root:
            return root
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.right:
                root = root.left
            elif not root.left:
                root = root.right
            else:
                val = self.findMin(root.right)
                if val == None:
                    return None
                root.val = val
                root.right = self.deleteNode(root.right, root.val)
        return root

    def findMin(self, node: TreeNode) -> Optional[int]:
        if not node:
            return None
        right = self.findMin(node.right)
        left = self.findMin(node.left)

        if left == None and right == None:
            return node.val
        elif left == None:
            return min(node.val, right)
        elif right == None:
            return min(node.val, left)

        return min(node.val, min(left, right))