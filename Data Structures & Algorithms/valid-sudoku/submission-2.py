class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for i, row in enumerate(board):
            for j, c in enumerate(row):
                if c != '.':
                    row_key = (i, c)
                    col_key = (c, j)
                    box_key = (i // 3, j // 3, c)
                    if row_key in seen or col_key in seen or box_key in seen:
                        return False
                    seen.add(row_key)
                    seen.add(col_key)
                    seen.add(box_key)
        return True