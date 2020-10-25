class Solution:
    def __init__(self):
        self.seen = {}

    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        elif N == 1:
            return 1
        elif N in self.seen:
            return self.seen[N]
        else:
            res = self.fib(N - 1) + self.fib(N - 2)
            self.seen[N] = res
            return res

