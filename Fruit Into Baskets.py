from typing import List

class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        """
        :param tree:
        :return:
        working theory: f1 is set to the first fruit seen; f2 is set to the next type of fruit seen that is different
        form f1
        then follow the command sequence until a fail. return the count. to make sure all possibilities are accounted
        for, always return to the point of f2 initialization and repeat
        """

        max_sum = 0

        i = 1
        next_start = 0
        f1 = tree[0]
        f2 = None

        temp_sum = 1

        while i < len(tree):
            if tree[i] == f1 or tree[i] == f2:
                temp_sum += 1
                i += 1
            elif tree[i] != f1 and f2 is None:
                f2 = tree[i]
                next_start = i
                temp_sum += 1
                i += 1
            elif tree[i] != f1 and f2 is not None:
                max_sum = max(temp_sum, max_sum)
                i = next_start
                f1 = tree[i]
                f2 = None
                temp_sum = 0
        max_sum = max(temp_sum, max_sum)
        return max_sum

