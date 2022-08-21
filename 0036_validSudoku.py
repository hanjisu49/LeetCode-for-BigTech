class Solution(object):
    def isValidSudoku(self, board):
        return (self.isRowValid(board) and self.isColValid(board) and self.isBoxValid(board))

    # 1. no iterations in the row
    def isRowValid(self, board):
        for row in board:
            if not self.isNotRepetitive(row):
                return False
        return True

    # 2. no iterations in the col
    def isColValid(self, board):
        for col in zip(*board):
            if not self.isNotRepetitive(col):
                return False
        return True

    # 3. no iterations in the box
    def isBoxValid(self, board):
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                box = []
                for x in (i, i+3):
                    for y in (j, j+3):
                        box.append(board[x][y])
                        if not self.isNotRepetitive(box):
                            return False
                return True

    # 4. check if there are only 1 to 9
    def isNotRepetitive(self, cells):
        nums = []
        for i in cells:
            if i != ".":
                nums.append(i)
        
        return len(set(nums)) == len(nums)
