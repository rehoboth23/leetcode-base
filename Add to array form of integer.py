from typing import List


class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        res = int("".join("{}".format(x) for x in A)) + K

        return [int(x) for x in str(res)]