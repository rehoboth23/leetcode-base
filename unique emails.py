from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        s = set()

        for email in emails:
            s.add(self.parseEmail(email))
        return len(s)

    def parseEmail(self, s: str) -> str:
        res = []
        local = s.split("@")
        for i in local[0]:
            if i == "+":
                break
            elif i != ".":
                res.append(i)

        return "".join(res) + "@" + local[1]