class Solution:
    def reverseWords(self, s: str) -> str:
        """

        :param s: string to reverse
        :return: reversed string
        working theory: to get every word, start at some point and go until a space is seen in from of the word
        then add the inverted version of that sequence to the result
        if a space is seen, add a space
        if at end of string, add word at last valid sequence
        the pre pointer points to beginning of last no space sequence
        """
        res = ""
        pre = 0
        for i in range(len(s)):
            if i < len(s) - 1 and s[i + 1] == " ":
                res += s[pre:i + 1][::-1]
            elif s[i] == " ":
                res += " "
                pre = i + 1
            elif i == len(s) - 1:
                res += s[pre:][::-1]
        return res
