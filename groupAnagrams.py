from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        :param strs: list of strings
        :return: strings group by anagrams
        working theory: sort the string as a list and group them using a hash set
        """
        strmap = {}
        for i in strs:
            x = "".join(sorted(list(i)))
            strmap[x] = [i] if x not in strmap else strmap[x] + [i]
        return strmap.values()