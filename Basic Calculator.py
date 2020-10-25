class Solution1:
    def calculate(self, s: str) -> int:
        """

        :param s: input expression string
        :return: result as an int
        working theory:

        this is particularly convoluted and quite difficult implementation to understand
        there are many more efficient algorithms online, but this is the one I derived to solve this problem

        the theory is to read the numbers into the number array in a polarized way i.e. positive or negative

        when some break point is reached, i.e. a close parenthesis or string end
        all numbers in array for a specific range are summed. This is a vector sum as they are stored with their signs
        the range is determined by the count variable. The count variable simply tells us how many numbers to take off
        the end of the list

        the count variable is increased everytime we see a sign.
        if an opening parenthesis is seen,the count variable is stored, then reset. when a close parenthesis is
        passed through, the count variable is set the last item in the stored counts array

        at the end, any built number and signs are accounted for by doing a naive sum, then emptying out the sign array
        by successive multiplications

        i have attached the official solution at the bottom
        """
        def getresult(arr, times):
            num1 = int(arr.pop())
            for i in range(times):
                num2 = int(arr.pop()) if len(arr) > 0 else 0
                num1 = num2 + num1

            return num1

        num_arr = []
        sign_arr = []
        sign_break = []

        temp_num = ""
        count = 0

        nums = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "0"}
        for i in range(len(s)):
            if i == " ":
                if temp_num != "":
                    if not sign_arr:
                        sign_arr.append("+")
                    num_arr.append(int(sign_arr.pop() + temp_num))
                temp_num = ""

            elif s[i] == "+" or s[i] == "-":
                count += 1
                if temp_num != "":
                    if not sign_arr:
                        sign_arr.append("+")
                    num_arr.append(int(sign_arr.pop() + temp_num))
                temp_num = ""
                sign_arr.append(s[i])

            elif s[i] == "(":
                sign_arr.append("+")
                sign_break.append(count)
                count = 0
                if temp_num != "":
                    num_arr.append(int(sign_arr.pop() + temp_num))
                temp_num = ""

            elif s[i] == ")":
                if temp_num != "":
                    if not sign_arr:
                        sign_arr.append("+")
                    num_arr.append(int(sign_arr.pop() + temp_num))
                temp_num = ""
                num_arr.append(getresult(num_arr, count))
                if not sign_arr:
                    sign_arr.append("+")
                num_arr.append(int(sign_arr.pop() + "1") * num_arr.pop())
                count = sign_break.pop()

            elif s[i] in nums:
                temp_num += s[i]

        if temp_num != "":
            if not sign_arr:
                sign_arr.append("+")
            num_arr.append(int(sign_arr.pop() + temp_num))
        num_arr.append(getresult(num_arr, count))

        while sign_arr:
            num_arr.append(int(sign_arr.pop() + "1") * num_arr.pop())

        return num_arr.pop()


class Solution2:
    def calculate(self, s: str) -> int:
        """
        this is the official solution offered by leetcode
        """

        stack = []
        operand = 0
        res = 0 # For the on-going result
        sign = 1 # 1 means positive, -1 means negative

        for ch in s:
            if ch.isdigit():

                # Forming operand, since it could be more than one digit
                operand = (operand * 10) + int(ch)

            elif ch == '+':

                # Evaluate the expression to the left,
                # with result, sign, operand
                res += sign * operand

                # Save the recently encountered '+' sign
                sign = 1

                # Reset operand
                operand = 0

            elif ch == '-':

                res += sign * operand
                sign = -1
                operand = 0

            elif ch == '(':

                # Push the result and sign on to the stack, for later
                # We push the result first, then sign
                stack.append(res)
                stack.append(sign)

                # Reset operand and result, as if new evaluation begins for the new sub-expression
                sign = 1
                res = 0

            elif ch == ')':

                # Evaluate the expression to the left
                # with result, sign and operand
                res += sign * operand

                # ')' marks end of expression within a set of parenthesis
                # Its result is multiplied with sign on top of stack
                # as stack.pop() is the sign before the parenthesis
                res *= stack.pop() # stack pop 1, sign

                # Then add to the next operand on the top.
                # as stack.pop() is the result calculated before this parenthesis
                # (operand on stack) + (sign on stack * (result from parenthesis))
                res += stack.pop() # stack pop 2, operand

                # Reset the operand
                operand = 0

        return res + sign * operand
