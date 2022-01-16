class Solution:
    def validateRows(self, board):
        for i in range(len(board)):
            tracker = []
            for j in range(len(board[i])):
                if board[i][j] in tracker and board[i][j] != ".":
                    print("row", i, j)
                    return False
                else:
                    tracker.append(board[i][j])
                    
        return True
        
    def validateColumns(self, board):
        for j in range(len(board[0])):
            tracker = []
            for i in range(len(board)):
                if board[i][j] in tracker and board[i][j] != ".":
                    print("column", i, j)
                    return False
                else:
                    tracker.append(board[i][j])
                    
        return True
        
    def validateBoxes(self, board):
        for i in range(3):
            for j in range(3):
                tracker = []
                for x in range(i*3, (i+1)*3):
                    for y in range(j*3, (j+1)*3):
                        if board[x][y] in tracker and board[x][y] != ".":
                            print("box", x, y)
                            return False
                        else:
                            tracker.append(board[x][y])
                    
        return True
                
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        isValid = True
        
        isValid = self.validateRows(board)
        isValid = isValid and self.validateColumns(board)
        isValid = isValid and self.validateBoxes(board)
        
        return isValid
        