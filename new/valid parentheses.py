class Solution:
    """
    using stacks
    """
    def isValid(self, s: str) -> bool:

        conjugates: dict = {")": "(", "]": "[", "}": "{"}
        opens: set = {"(", "[", "{"}

        stack: [str] = []

        for char in s:
            if char in opens:
                stack.append(char)
            else:
                if stack:
                    opp: str = stack.pop()
                    if opp != conjugates[char]:
                        return False
                else:
                    return False

        return stack == []