# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def splitBST(self, root: TreeNode, V: int) -> List[TreeNode]:
        if not root:
            return [root, root]

        self.res = TreeNode(float('inf'))
        def insertnode(node, newnode):
            if not node:
                return newnode
            if node.val > newnode.val:
                node.left = insertnode(node.left, newnode)
            elif node.val < newnode.val:
                node.right = insertnode(node.right, newnode)
            return node

        def find(node, key):
            if not node:
                return None
            if node.val <= key:
                res = node.right
                node.right = None
                insertnode(self.res, node)
                return find(res, key)
            elif node.val > key:
                node.left = find(node.left, key)
                return node

        root = find(root, V)
        return [self.res.left, root]


