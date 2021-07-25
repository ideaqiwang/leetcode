'''
329. Longest Increasing Path in a Matrix

Given an m x n integers matrix, return the length of the longest increasing path in matrix.
From each cell, you can either move in four directions: left, right, up, or down.
You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

Example 1:
Input: matrix = [[9,9,4],
                 [6,6,8],
                 [2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].
'''

class Solution:
    # Memoriaztion
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memo = {}
        longest = 1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                longest = max(longest, self.dfs(matrix, i, j, memo))
        return longest        
        
        
    def dfs(self, matrix, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]
        
        longest = 1
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            x, y = i+dx, j+dy
            if self.isValid(matrix, x, y) and matrix[x][y] > matrix[i][j]:
                longest = max(longest, self.dfs(matrix, x, y, memo)+1)
        
        memo[(i, j)] = longest
        return longest
        
        
    def isValid(self, matrix, x, y):
        return 0<=x<len(matrix) and 0<=y<len(matrix[0])
