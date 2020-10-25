from collections import Counter
class Solution:
    """
    uses set theory
    """
    def intersect(self, nums1: [int], nums2: [int]) -> [int]:
        count1 = Counter(nums1)
        count2 = Counter(nums2)
        res = []
        for i in count1:
            if i in count2: res.extend([i]*min(count1[i], count2[i]))
        return res
