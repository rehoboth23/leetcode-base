class Solution:
    """
    working theory: if the sum of the current sum and the index at i is less than the index at i; generally only
    possible for the sum of negative numbers, set the current sum to the index at i, otherwise add the index at i to the
    current sum, use a max to set the value of the max_sum at every iteration
    """
    def maxSubArray(self, nums: [int]) -> int:
        max_sum = curr_sum = nums[0]
        size = len(nums)
        for i in range(1, size):
            curr_sum = max(nums[i], curr_sum + nums[i])
            max_sum = max(max_sum, curr_sum)
        return max_sum


class Solution2:
    @staticmethod
    def maxSubRange(self, nums: [int]) -> [int]:
        max_sum = curr_sum = 0
        start = 0
        stop = 0
        t_start = 0
        t_stop = 0

        for idx, num in enumerate(nums):
            curr_sum = max(num, curr_sum + num)
            max_sum = max(curr_sum, max_sum)
        return max_sum


a = [1, 2, 3, -4, -5, 6, 7, -13, 9]

print(Solution2.maxSubRange(None, a))