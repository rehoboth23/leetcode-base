from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        i = len(arr) - 1
        max_n = arr[i]

        while i > -1:
            if i == len(arr) - 1:
                arr[i] = -1
            else:
                temp = arr[i]
                arr[i] = max_n
                max_n = max(temp, max_n)

            i -= 1
        return arr