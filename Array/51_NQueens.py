'''
51. N-Queens

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.
Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

Example 1:
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
'''

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [['.'] * n for _ in range(n)]
        
        self.dfs(board, n, 0, set(), set(), set(), res)
        return res

    def dfs(self, board, n, row, diagonals, antiDiagonals, cols, res):
        if row == n:
            res.append(self.createBoard(board))
            return
        
        for col in range(n):
            curDiagonal = row - col
            curAntiDiagonal = row + col
            if col in cols or curDiagonal in diagonals or curAntiDiagonal in antiDiagonals:
                continue
            
            cols.add(col)
            diagonals.add(curDiagonal)
            antiDiagonals.add(curAntiDiagonal)
            board[row][col] = 'Q'
            
            self.dfs(board, n, row+1, diagonals, antiDiagonals, cols, res)
            
            cols.remove(col)
            diagonals.remove(curDiagonal)
            antiDiagonals.remove(curAntiDiagonal)
            board[row][col] = '.'    
    
    def createBoard(self, board):
        res = []
        for i in range(len(board)):
            res.append(''.join(board[i]))
        return res
