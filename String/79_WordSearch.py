'''
79. Word Search

Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring.
The same letter cell may not be used more than once.

Example 1:
Input: board = [["A","B","C","E"],
                ["S","F","C","S"],
                ["A","D","E","E"]],
       word = "ABCCED"
Output: true
'''

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if self.dfs(board, i, j, word):
                    return True
        return False
                    
    def dfs(self, board, i, j, suffix):
        if not suffix:
            return True

        if not self.isValid(board, i, j) or board[i][j] != suffix[0]:
            return False
        
        ret = False
        board[i][j] = '#'
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ret = self.dfs(board, i+dx, j+dy, suffix[1:])
            if ret:
                break
        board[i][j] = suffix[0]
        return ret
            
    def isValid(self, board, x, y):
        return 0<=x<len(board) and 0<=y<len(board[0])
