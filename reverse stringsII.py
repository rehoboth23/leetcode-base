class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        """
        :param s: string to be reversed
        :param k: number of chars to reverse
        :return: reversed string by k
        """
        res = ""  # result string
        size = len(s)  # length of string
        i = 0  # counter i
        while True:

            # if remaining chars < 2k, add the concat the flip of k chars and next k chars to res
            if size - i >= 2 * k:
                res += s[i:i + k][::-1] + s[i + k: i + 2 * k]
            # if remaining chars > k but remaining chars < 2k add the flip ot first k chars and the rest and add to res
            elif k <= size - i < 2 * k:
                res += s[i:i + k][::-1] + s[i + k:]
            # if remaining chars less than k reverse the rest and add to res then break
            elif size - i < k:
                res += s[i:i + k][::-1]
                break

            # always increment i by 2k
            i += 2 * k

        return res
