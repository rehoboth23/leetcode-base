class Number:
    def __init__(self, val):
        self.val = val

    def __str__(self):
        return str(self.val)

    def __lt__(self, other):
        return self.val % 2 == 0 and other.val % 2 == 1

    def __gt__(self, other):
        return self.val % 2 == 1 and other.val % 2 == 0

    def __eq__(self, other):
        return self.val % 2 == 0 and other.val % 2 == 0

    def __le__(self, other):
        return self.val % 2 == 0 and other.val % 2 == 1 or self.val % 2 == 0 and other.val % 2 == 0

    def __ge__(self, other):
        return self.val % 2 == 1 and other.val % 2 == 0 or self.val % 2 == 1 and other.val % 2 == 1


class Solution:
    def sortArrayByParity(self, A: [int]) -> [int]:
        nums = [Number(x) for x in A]
        nums.sort()

        res = [x.val for x in nums]
        return res