class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        sudoku = set()
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.': continue
                num = board[i][j]
                if (i,num) in sudoku or \
                    (num,j) in sudoku or \
                    (i // 3, j // 3, num) in sudoku:
                    return False
                sudoku.add((i, num)
                sudoku.add(num, j))
                sudoku.add((i // 3, j // 3, num)
        return True


sol = Solution()
board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
print(sol.isValidSudoku(board))