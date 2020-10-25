class Solution:
    def orderlyQueue(self, S: str, K: int) -> str:
        """

        :param S: the string to sort
        :param K: the
        :return: altered string
        working theory: for any k greater than one, the string is just going to be sorted
        for k at one, make the string an array
        remove the first item and inset at the end
        compare it to whatever was previously our result
        then if it checks out do a deep copy of the temp into the result
        return the result as a string
        """
        if K > 1:
            return "".join(sorted(S))
        res = list(S)
        temp = list(S)

        for i in range(len(temp) - 1):
            temp.append(temp.pop(0))
            if temp < res:
                res = [x for x in temp]
        return "".join(res)