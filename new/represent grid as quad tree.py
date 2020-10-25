"""
# Definition for a QuadTree node.
"""
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: [[int]]) -> 'Node':

        def checkValues(grid_arr, start_row, stop_row, start_col, stop_col):
            pre = grid_arr[start_row][start_col]

            for r in range(start_row, stop_row):
                for c in range(start_col, stop_col):
                    if grid[r][c] != pre: return False, 1

            return True, pre

        def makeQuads(grid_arr, start_row, stop_row, start_col, stop_col):
            check, val = checkValues(grid, start_row, stop_row, start_col, stop_col)
            if check:
                return Node(val, 1, None, None, None, None)
            else:
                s1 = (stop_row + start_row) // 2
                s2 = (start_col + stop_col) // 2
                top_left = makeQuads(grid_arr, start_row, s1, start_col, s2)
                top_right = makeQuads(grid_arr, start_row, s1, s2, stop_col)
                bottom_left = makeQuads(grid_arr, s1, stop_row, start_col, s2)
                bottom_right = makeQuads(grid_arr, s1, stop_row, s2, stop_col)
                return Node(val, 0, top_left, top_right, bottom_left, bottom_right)

        size = len(grid)
        return makeQuads(grid, 0, size, 0, size)

