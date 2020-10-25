class Solution2:
    from collections import Counter
    def findMaxConsecutiveOnes(self, nums: [int]) -> int:
        """
        working solution:
        if a zero is seen, the current count which is the sum of valid windows up until that point is compared with the
        max count and the max count set appropriately. the current count is then set to the difference of the last seen
        zero and the current index -1; this effectively counts all valid ones from then until now.
        compare at end before return to ensure best answer.
        """
        zero_index = -1
        current_count = 0
        max_count = 0

        for index, num in enumerate(nums):
            if not num:
                max_count = max(max_count, current_count)
                current_count = index - zero_index - 1
                zero_index = index
            current_count += 1
        return max(max_count, current_count)

