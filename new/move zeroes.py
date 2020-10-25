from typing import List


class Solution:
    from collections import Counter
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def findNonZero(subarr):
            for i in range(len(subarr)):
                if subarr[i] != 0:
                    return i
            return -1

        curr = 0
        while curr < len(nums) - 1:
            if nums[curr] == 0:
                x = findNonZero(nums[curr:])
                if x == -1:
                    break
                nums[curr], nums[curr + x] = nums[curr + x], nums[curr]

            curr += 1
