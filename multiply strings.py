class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """
        :param num1: the first number as a string
        :param num2: the second number as a string
        :return: the product as a string
        working theory:
        zeroPad: the power of 10 to muliply by at every stage
        res = result as an integer; it is better because string conversion will only happen once and direct addition is
        allowed
        num1, and num2 are reversed to work from the back
        """
        zeroPad = 0
        res = 0
        num1 = num1[::-1]
        num2 = num2[::-1]
        for i in num1:
            res += self.multiplyHelp(num2, i, zeroPad)
            zeroPad += 1
        return "{}".format(res)

    def multiplyHelp(self, target: str, actor: str, pos: int) -> int:
        """
        :param target: the multiplication target
        :param actor: the actor is the one number by which all members of the target are multiplied
        :param pos: the pos is the power to which ten is raised to as to be multiplied by the result
        :return: number result
        working theory: using a result, remainder_model(next_q)
        read the comments in the lines
        modulus 10 gives product value for any multiplication round
        integer division by 10 gives the carry over
        account for any last carry overs at the end
        since the list is flipped, flip the list, concatenate the characters, convert to integer and return integer
        """
        res = ["0"] * pos
        multiplier = int(actor)
        next_q = 0
        for i in target:
            # convert number to int
            x = int(i)

            # find the product and add any previous carry overs
            product = multiplier * x + next_q
            next_q = 0  # reset remainder count

            # get the remainder of the product
            r = product % 10

            # get the carry over
            q = product // 10

            # get the carry over
            next_q = q

            # add r to result list
            res.append("{}".format(r))
        # account for any remaining carry overs
        if next_q > 0:
            res.append("{}".format(next_q))

        # convert the reversed list into an integer
        num = int("".join(x for x in res[::-1]))
        return num


