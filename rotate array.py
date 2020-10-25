from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> [int]:
        """
        Do not return anything, modify nums in-place instead.
        working theory is to remove the last element and insert at the start k times
        """
        for i in range(k):
            nums.insert(0, nums.pop())
