def findLength(self, A, B):
    B, A = sorted([A, B], key=len)
    m = len(A)
    n = len(B)
    maxLen = 0
    for a in range(-n + 1, m + n - 1):
        cnt = 0
        for ptrB in range(n):
            ptrA = a + ptrB
            if ptrA < 0: continue
            if ptrA >= m: break
            if A[ptrA] == B[ptrB]:
                cnt += 1
                if cnt > maxLen: maxLen = cnt
            else:
                cnt = 0
    return maxLen


"""uses a grid to check for a repetition"""
class Solution(object):
    def findLength(self, A, B):
        memo = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
        for i in range(len(A) - 1, -1, -1):
            for j in range(len(B) - 1, -1, -1):
                if A[i] == B[j]:
                    memo[i][j] = memo[i+1][j+1]+1
        return max(max(row) for row in memo)

