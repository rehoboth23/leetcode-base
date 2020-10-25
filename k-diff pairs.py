from typing import List


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        """

        :param nums: array of numbers
        :param k: difference
        :return: number of suitable pairs
        use conjugate/pair tagging in a hash set to track what has been seen
        return the length of the set of pairs
        """

        pairs: set = set()
        seen: set = set()

        for i in nums:
            c1 = k - i
            c2 = k + i
            print(i, k, c1, c2)
            if c1 in seen and abs(c1 - i) == k:
                pairs.add((max(c1, i), min(c1, i)))
            elif -c1 in seen and abs(-c1 - i) == k:
                pairs.add((max(-c1, i), min(-c1, i)))

            if c2 in seen and abs(c2 - i) == k:
                pairs.add((max(c2, i), min(c2, i)))
            elif -c2 in seen and abs(-c2 - i) == k:
                pairs.add((max(-c2, i), min(-c2, i)))
            seen.add(i)
        print(pairs)
        return len(pairs)