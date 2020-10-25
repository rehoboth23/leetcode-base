class Solution:
    def __init__(self):
        self.seen = {}

    def tribonacci(self, n: int) -> int:
        if n == 0: return 0
        if n == 1 or n == 2:
            return 1
        elif n in self.seen:
            return self.seen[n]
        else:
            res = self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)
            self.seen[n] = res
            return res
