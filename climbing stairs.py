class Solution:
    """
    memoized DFS; we could also try a greedy first search from the end of the arr;
    """
    def __init__(self):
        self.seen = {}

    def climbStairs(self, n: int) -> int:
        def climb(i, n):
            if i == n:
                return 1
            elif i > n:
                return 0
            elif i in self.seen:
                    return self.seen[i]
            else:
                res = climb(i+1, n) + climb(i+2, n)
                self.seen[i] = res
                return res
        return climb(0, n)