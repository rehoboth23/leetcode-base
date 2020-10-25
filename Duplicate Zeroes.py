from typing import List


class Solution:
    """
    funny solution that adds all new zeroes to the list then pops off the difference in list lenght
    """
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        size = len(arr)
        i = 0
        while i < len(arr):
            if arr[i] == 0: arr.insert(i, 0); i += 2
            else: i += 1
        diff = len(arr) - size
        for i in range(diff):
            arr.pop()


class Solution2:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        This cascades the list. Cascading is a ripple effect that sets the value of of an elements next element to it
        self. this way all the zeroes are duplicated and the extra numbers are removed
        """

        def cascade(rarr, start):
            if rarr:
                temp = rarr[start]
                for i in range(start + 1, len(rarr)):
                    rtemp = rarr[i]
                    rarr[i] = temp
                    temp = rtemp

        i = 0
        while i < len(arr):
            if arr[i] == 0:
                cascade(arr, i); i += 2
            else:
                i += 1



