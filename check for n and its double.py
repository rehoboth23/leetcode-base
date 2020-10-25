class Solution:
    """
    use set matching theory; check first then add last to account for 0
    """
    def checkIfExist(self, arr: [int]) -> bool:
        s = set()
        for i in arr:
            if 2 * i in s:
                return True
            if i / 2 in s:
                return True
            s.add(i)