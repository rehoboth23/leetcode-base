from typing import List


class Solution:
    """
    uses a duplicate sorted list
    """
    def heightChecker(self, heights: List[int]) -> int:
        res = sorted(heights)
        count = 0
        for i in range(len(res)):
            if res[i] != heights[i]: count += 1

        return count