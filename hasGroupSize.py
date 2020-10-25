from typing import List

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        """
        :param deck: array of cards
        :return: if the array can be split into equal groups of equal length all containing unique numbers
        return false if one card in deck
        find how much of each card is in the deck
        find the minimum number of card of any cards
        check if all the cards have a common factor; limit by minimum length card stack
        return if they have a common factor
        """
        if len(deck) < 2:
            return False
        map_ints = {}
        for i in deck:
            map_ints[i] = 1 if i not in map_ints else map_ints[i] + 1

        min_sum = float('inf')

        for i in map_ints:
            min_sum = min(map_ints[i], min_sum)

        i = 2 if min_sum % 2 == 0 else 3
        while i <= min_sum:
            count = 0
            for x in map_ints:
                count = count + 1 if map_ints[x] % i == 0 else count
            if count == len(map_ints):
                return True
            else:
                i += 1
        return False