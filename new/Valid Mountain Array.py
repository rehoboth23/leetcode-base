class Solution:
    def validMountainArray(self, A: [int]) -> bool:
        if len(A) < 3:
            return False
        direction = 1
        for i in range(1, len(A)):
            if A[i] == A[i - 1]:
                return False
            elif A[i] < A[i - 1] and i > 1:
                direction = -1
            elif A[i] < A[i - 1] and direction == 1:
                return False
            elif A[i] > A[i - 1] and direction == -1:
                return False

        return direction == -1
