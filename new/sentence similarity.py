class Solution:
    """
    using sets to track similar pairs
    """
    def areSentencesSimilar(self, sentence1: [str], sentence2: [str], similarPairs: [[str]]) -> bool:
        l1: int = len(sentence1)
        l2: int = len(sentence2)

        if l1 != l2: return False
        pair_set: set = set()
        for pair in similarPairs:
            pair_set.add((pair[0], pair[1]))
            pair_set.add((pair[1], pair[0]))

        pair_set = pair_set.union(set([(x, x) for x in sentence1]))
        pair_set = pair_set.union(set([(x, x) for x in sentence2]))

        for x in range(l1):
            if not ((sentence1[x], sentence2[x]) in pair_set or (sentence2[x], sentence1[x]) in pair_set):
                return False

        return True