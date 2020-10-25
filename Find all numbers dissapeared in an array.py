class Solution:
    """
    using set theory of intersection
    """
    def findDisappearedNumbers(self, nums: [int]) -> [int]:
        if not nums:
            return nums
        s1 = set(nums)
        s2 = set([x for x in range(1, len(nums)+1)])
        return list(s2-s1)
