class Solution:
    def reverseWords(self, s: str) -> str:
        """
        :param s: string to be reversed
        :return: reverse string
        working theory: split the string at the spaces and save as array
        build the new string from reversed array
        to omit extra spaces, join by spaces and ignors empty strings in array i.e. [""]
        """
        splits = s.split(" ")
        res = [x for x in splits[::-1] if x != ""]
        return " ".join(res)