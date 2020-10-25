import math


def solve(num, lowerEnd, upperEnd):
    res = []

    even = upperEnd % 2 == 0
    rise = num // 2 - 1
    come_down = num // 2 + 1

    if upperEnd - rise < lowerEnd or upperEnd - come_down < lowerEnd:
        return -1
    i = 1
    while i <= come_down:
        if rise >= 0:
            res.append(upperEnd - rise)
            rise -= 1
        else:
            res.append(upperEnd - i)
            i += 1
    return res


print(solve(5, 2, 6))