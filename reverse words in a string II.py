from typing import List


class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        working theory: the first break point is 0
        string is represented as an array
        remove last character and insert the characters into string at break point
        if a space is seen, set break point to i (i is counting up) so i = no of changes
        insert the space and increment break point again also increment i to keep pace with the number of altered characters
        a continue can be used here  ut is unecessary
        """
        insert = 0
        i = 0
        while i < len(s):
            print(s[len(s)-1])
            if s[len(s)-1] == " ":
                insert = i
                s.insert(insert, s.pop())
                insert += 1
                i += 1
            s.insert(insert, s.pop())
            i += 1