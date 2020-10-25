# Definition for a binary tree node.

from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
class Solution:
    """
    go down tree, using recursion and an array, look for nodes that have only one child and add the child to the array.
    base case when a node has no children
    """
    def getLonelyNodes(self, root: TreeNode) -> List[int]:
        res = []
        self.findLonelyNodes(root, res)
        return res

    def findLonelyNodes(self, node: TreeNode, lonelyNodes: [int]):
        if not (node.left or node.right):
            return
        if node.left:
            if not node.right:
                lonelyNodes.append(node.left.val)
            self.findLonelyNodes(node.left, lonelyNodes)
        if node.right:
            if not node.left:
                lonelyNodes.append(node.right.val)
            self.findLonelyNodes(node.right, lonelyNodes)
