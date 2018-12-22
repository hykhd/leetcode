class Solution:
    def __init__(self):
        self.num_set = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.row = [set() for _ in range(9)]
        self.col = [set() for _ in range(9)]
        self.grid = [[set() for _ in range(3)] for _ in range(3)]
        self.empty_grid = []

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        for i in range(9):
            for j in range(9):
                sub = board[i][j]
                if sub == '.':
                    self.empty_grid.append((i, j))
                else:
                    self.row[i].add(sub)
                    self.col[j].add(sub)
                    self.grid[i // 3][j // 3].add(sub)
        self.DFS(0, board)
        # print(self.empty_grid)
        # if self.DFS(0, board):
        #     print(board)
        # print(board)

    def DFS(self, index, board):
        num = list(self.num_set)
        i, j = self.empty_grid[index]
        if index == 11:
            pass
        for value in num:
            if self.judge(i, j, value):
                self.row[i].add(value)
                self.col[j].add(value)
                self.grid[i // 3][j // 3].add(value)
                board[i][j] = value
                if index == len(self.empty_grid) - 1:
                    return True
                else:
                    index = index + 1
                    if not self.DFS(index, board):
                        self.row[i].remove(value)
                        self.col[j].remove(value)
                        self.grid[i // 3][j // 3].remove(value)
                        board[i][j] = '.'
                        index = index - 1
                    else:
                        return True
        return False

    def judge(self, i, j, value):
        if value in self.row[i] or value in self.col[j] or value in self.grid[
                i // 3][j // 3]:
            return False
        return True


sol = Solution()
board = [[".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."]]
print(sol.solveSudoku(board))