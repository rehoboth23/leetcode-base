class Solution:
    def areSentencesSimilarTwo(self, words1: [str], words2: [str], pairs: [[str]]) -> bool:

        l1: int = len(words1)
        l2: int = len(words2)

        if l1 != l2: return False

        def merge(pair_words, key, val):
            for x in pair_words[key]:
                pair_words[x] = pair_words[x].union({val})
                pair_words[val] = pair_words[val].union({x})

        pair_words = {}

        for pair in pairs:
            word1 = pair[0]
            word2 = pair[1]

            pair_words[word1] = {word2} if not word1 in pair_words else pair_words[word1].union({word2})
            pair_words[word2] = {word1} if not word2 in pair_words else pair_words[word2].union({word1})

            merge(pair_words, word1, word2)
            merge(pair_words, word2, word1)

        for word in words1:
            pair_words[word] = {word} if word not in pair_words else pair_words[word]

        for word in words2:
            pair_words[word] = {word} if word not in pair_words else pair_words[word]

        for idx, word in enumerate(words1):
            check = pair_words[word].intersection(pair_words[words2[idx]])
            if not check: return False

        return True
