class Solution:
    """
    uses set matching. if a number is in the set returns true, otherwise puts the number in the set
    if true is never returned returns false
    """
    def containsDuplicate(self, nums: [int]) -> bool:
        s: set = set()
        for i in nums:
            if i in s: return True
            s.add(i)
        return False
