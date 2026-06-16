class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            for j in range(9):
                if board[i][j]=='.':
                    continue
                num=board[i][j]
                for col in range(9):
                    if col!=j and board[i][col]==num:
                        return False
                for row in range(9):
                    if row!=i and board[row][j]==num:
                        return False
                startrow=(i//3)*3
                startcol=(j//3)*3
                for r in range (startrow,startrow+3):
                    for c in range(startcol,startcol+3):
                        if (r!=i and c!=j) and board[r][c]==num:
                            return False
        return True