# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        """
        :param root: root node
        :return: personal tilt of the node
        this is a brute force appraoch
        recursively sum personal tilts of the node
        for every node use the node sum method to find the sum of left and right branches
        find the node tilt, return sum of left tilt, right tilt and node tilt
        null nodes have 0 tilts
        """
        if root == None:
            return 0
        lval = 0
        rval = 0
        personalTilt = 0
        if root.left != None:
            lval += self.nodeSum(root.left)
            personalTilt += self.findTilt(root.left)
        if root.right != None:
            rval += self.nodeSum(root.right)
            personalTilt += self.findTilt(root.right)
        personalTilt += abs(lval - rval)
        return personalTilt

    def nodeSum(self, node):
        if (node == None):
            return 0
        else:
            return node.val + self.nodeSum(node.left) + self.nodeSum(node.right)


class Solution2:
    """
    optimized solution
    create a new function that recursively calculates node sums and total tile
    when a null node is reached it returns 0 tilt and 0 sum
    for non null nodes, return their tilt+tilt sum returned and thier left sum+right sum+node val
    call the function in out main
    return 0 index of final tuple
    """

    def findTilt(self, root: TreeNode) -> int:
        def calc_tilts(root):
            if not root:
                return 0, 0
            ltilt, lsum = calc_tilts(root.left)
            rtilt, rsum = calc_tilts(root.right)
            return ltilt + rtilt + abs(lsum - rsum), lsum + rsum + root.val

        return calc_tilts(root)[0]

