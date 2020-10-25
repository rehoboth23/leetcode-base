from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums[i], nums[len(nums)-1] = nums[len(nums)-1], nums[i]
                nums.pop()
            else:
                i += 1
        return len(nums)
