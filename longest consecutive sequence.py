class Solution:
    """
    stores a previous value, checks for consecutivity, update the counters durins the loop
    check max at end
    """
    def longestConsecutive(self, nums: [int]) -> int:
        if not nums:
            return 0
        max_ln = 0
        curr_ln = 1
        nums.sort()
        pre = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == pre+1:
                pre = nums[i]
                curr_ln += 1
            elif nums[i] == pre:
                continue
            else:
                max_ln = max(curr_ln, max_ln)
                curr_ln = 1
                pre = nums[i]
        max_ln = max(curr_ln, max_ln)
        return max_ln