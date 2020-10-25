from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        scount = Counter(s)
        tcount = Counter(t)

        for c in scount:
            if not (c in scount and c in tcount): return False
            if (c in scount and c in tcount) and scount[c] != tcount[c]: return False
        return True
