from typing import List


class Solution:
    def longestMountain(self, A: List[int]) -> int:
        """
        :param A: the list to find the mountain in
        :return: length of largest mountain; 0 if no mountains
        the direction 1 denotes up, 0 denotes down
        the start give the start of the mountain
        the stop gives the stop of the mountain
        i simply counts to the length of the array
        if at the end, and going up break loop, not necessary tho as loop will break on its own
        if at the end and going set res to the difference of stop and start plus 1
        if going up and a plateau is found, advance i set start to i continue
        if going down and flat ground is found, set if res < start-stop+1 reset res to start-stop+1
        advance i and set start to i
        if going up and up slope is found, advance i
        if going up and down slope is found, if the differnce between i and start is at least 1
        change direction and continue else advance i, set start to i and continue
        if going down and down slope is found, advance i
        if going down and up slope is found, change direction, reset res appropriately, set start to i and advance i
        """

        direction = 1

        i = 0
        start = 0
        stop = 0
        res = 0

        while i < len(A):
            if i == len(A) - 1:
                if direction == 1:
                    stop = i
                    if stop - start + 1 > res:
                        res = stop - start + 1
                    i += 1
            elif direction == 1 and A[i + 1] == A[i]:
                i += 1
                start = i
                continue
            elif direction == 0 and A[i + 1] == A[i]:
                stop = i
                if stop - start + 1 > res:
                    res = stop - start + 1
                i += 1
                start = i
                direction = 1
                continue
            elif direction == 1 and A[i + 1] > A[i]:
                i += 1
                continue
            elif direction == 1 and A[i + 1] < A[i]:
                if i - start > 0:
                    direction = 0
                    continue
                i += 1
                start = i
                continue
            elif direction == 0 and A[i + 1] < A[i]:
                i += 1
                continue
            elif direction == 0 and A[i + 1] > A[i]:
                stop = i
                if stop - start + 1 > res:
                    res = stop - start + 1
                start = i
                direction = 1
                continue

        return res



