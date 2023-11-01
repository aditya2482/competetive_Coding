import collections

class Solution:
    def isValidSudoku(self, board):
        hashrow = collections.defaultdict(set)
        hashcol = collections.defaultdict(set)
        sq = collections.defaultdict(set)

        for row in range(9):
            for column in range(9):
                if board[row][column] == ".":
                    continue
                if (board[row][column] in hashrow[row] or 
                board[row][column] in hashcol[column] or  
                board[row][column] in sq[(row//3),column//3]):
                    return False
                hashrow[row].add(board[row][column])
                hashcol[column].add(board[row][column])
                sq[(row//3),column//3].add(board[row][column])
        return True


board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
        