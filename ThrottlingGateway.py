from typing import List


def throttlingGateway(requestTime: List) -> int:
    count = 0
    dropped = {}
    rng = len(requestTime)
    for i in range(rng):
        k = requestTime[i]
        if i > 2 and k == requestTime[i-1]:
            if k not in dropped or dropped[k] != i:
                dropped[k] = i
                count += 1
        elif i > 19 and k - requestTime[i-20] < 10:
            if k not in dropped or dropped[k] != i:
                dropped[k] = i
                count += 1
        elif i > 59 and k - requestTime[i-60] < 60:
            if k not in dropped or dropped[k] != i:
                dropped[k] = i
                count += 1
    return count


# alternative
def droppedRequests(requestTime):
    # Write your code here

    drop1 = []
    drop20 = []
    drop60 = []
    i = 0
    for v in requestTime:
        while len(drop1) > 0 and v - drop1[0] >= 1:
            drop1.pop(0)
        while len(drop20) > 0 and v - drop20[0] >= 10:
            drop20.pop(0)
        while len(drop60) > 0 and v - drop60[0] >= 60:
            drop60.pop(0)
        drop = 0
        if len(drop1) < 3:
            drop1.append(v)
        else:
            drop = 1
            if len(drop1) > 0:
                drop1.pop(0)
                drop1.append(v)

        if len(drop20) < 20:
            drop20.append(v)
        else:
            drop = 1
            if len(drop20) > 0:
                drop20.pop(0)
                drop20.append(v)

        if len(drop60) < 60:
            drop60.append(v)
        else:
            drop = 1
            if len(drop60) > 0:
                drop60.pop(0)
                drop60.append(v)
        i += drop

    return i
