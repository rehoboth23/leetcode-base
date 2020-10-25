import math
from typing import List


class Solution:
    """
    evaluates only at operators
    inserts the value at the position of i -2
    decreases i to prevent skipping
    breaks when length of list is 1
    """
    def evalRPN(self, tokens: List[str]) -> int:
        i = 0
        while len(tokens) > 1:
            if tokens[i] == "/":
                a, b = int(tokens[i - 2]), int(tokens[i - 1])
                tokens.pop(i)
                tokens.pop(i - 1)
                tokens.pop(i - 2)
                res = a / b
                if res >= 0:
                    tokens.insert(i - 2, math.floor(res))
                else:
                    tokens.insert(i - 2, math.ceil(res))
                i -= 1
            elif tokens[i] == "*":
                a, b = int(tokens[i - 2]), int(tokens[i - 1])
                tokens.pop(i)
                tokens.pop(i - 1)
                tokens.pop(i - 2)
                tokens.insert(i - 2, a * b)
                i -= 1
            elif tokens[i] == "-":
                a, b = int(tokens[i - 2]), int(tokens[i - 1])
                tokens.pop(i)
                tokens.pop(i - 1)
                tokens.pop(i - 2)
                tokens.insert(i - 2, a - b)
                i -= 1
            elif tokens[i] == "+":
                a, b = int(tokens[i - 2]), int(tokens[i - 1])
                tokens.pop(i)
                tokens.pop(i - 1)
                tokens.pop(i - 2)
                tokens.insert(i - 2, a + b)
                i -= 1
            else:
                i += 1
        return int(tokens.pop())
