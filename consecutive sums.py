
def consecutiveSums(N):
    count = 0
    i = 0
    while i < N:
        if N == i + i+1:
            count += 1
        i += 1