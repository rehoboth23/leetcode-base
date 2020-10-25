class Solution:
    """
    linear time; linear space
    """
    def singleNumber(self, nums: [int]) -> int:
        s = set()
        for i in nums:
            if i not in s:
                s.add(i)
            else:
                s.remove(i)
        return s.pop()


class Solution2:
    """
    linear time; constant space
    """
    def singleNumber(self, nums: [int]) -> int:
        nums.sort()
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                i += 2
            else:
                return nums[i]
        return nums.pop()


class Solution3:
    """
    quadratic time; constant space
    """
    def singleNumber(self, nums: [int]) -> int:
        i = len(nums)-1
        nums.sort()
        while len(nums) > 1:
            if nums[i] == nums[i-1]:
                nums.pop(i)
                nums.pop(i-1)
                i -= 2
            else:
                i -= 1
        return nums[0]
