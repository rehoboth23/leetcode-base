from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """

        :param digits: array containing numbers
        :return: altered array
        working theory: when there is no remainder return the array,
        when the current index is the the first index and the first escape was not used, there must be a remainder
        insert 1 at first index then return the node
        """
        rem = 1
        for i in range(-1, -len(digits) - 1, -1):
            s = digits[i] + rem

            if s >= 10:
                rem = 1
                digits[i] = s - 10
                print(digits)
            else:
                digits[i] = s
                rem = 0
                return digits
            if i == -len(digits):
                digits.insert(0, 1)
                return digits
