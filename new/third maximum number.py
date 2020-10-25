class Solution:
    def thirdMax(self, nums: [int]) -> int:
        nums.sort(reverse=True)
        max_n = nums[0]
        count = 1
        for i in nums:
            if i < max_n: max_n = i; count += 1
            if count == 3: break
        return max_n if count == 3 else nums[0]


s = [9, 4, 5, 7, 2, 3]
ss = Solution()
print(ss.thirdMax(s))