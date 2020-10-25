class Solution:
    def __init__(self):
        self.N = None
        self.seen = {}
        self.arr = None

    def minCostClimbingStairs(self, cost: [int]) -> int:
        if not cost:
            return 0
        self.N = len(cost)
        self.arr = cost

        def climb(i):
            if i > self.N:
                return 0
            if i == self.N:
                return 0
            elif i == self.N - 1:
                return self.arr[i]
            elif i == self.N - 2:
                return self.arr[i]
            elif i in self.seen:
                return self.seen[i]
            else:
                res = min(climb(i + 1), climb(i + 2)) + self.arr[i]
                self.seen[i] = res
                return res

        return min(climb(0), climb(1))


