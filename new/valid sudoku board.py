from math import ceil


class Solution:
    def isValidSudoku(self, board: [[str]]) -> bool:

        rows: int = len(board)
        cols: int = len(board[0])
        seen: set = set()

        for r in range(rows):
            for c in range(cols):
                if board[r][c] != ".":
                    key1 = "{}, r{}".format(board[r][c], r)
                    key2 = "{}, c{}".format(board[r][c], c)
                    key3 = "{}, boxr{}, boxc{}".format(board[r][c], ceil(r // 3), ceil(c // 3))
                    if key1 in seen or key2 in seen or key3 in seen:
                        return False
                    seen.add(key1)
                    seen.add(key2)
                    seen.add(key3)
        return True

