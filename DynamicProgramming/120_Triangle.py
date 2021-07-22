'''
120. Triangle

Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

Example 1:
Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).

Example 2:
Input: triangle = [[-10]]
Output: -10
'''

class Solution1:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        self.memo = {}
        self.minSum = sys.maxsize
        return self.dfs(triangle, 0, 0, 0)
        
    def dfs(self, triangle, row, col, path):
        m = len(triangle)
        if row == m:
            return 0
        
        if (row, col) in self.memo:
            return self.memo[(row, col)]
        
        left = self.dfs(triangle, row+1, col, path)
        right = self.dfs(triangle, row+1, col+1, path)
        
        self.memo[(row, col)] = min(left, right)+triangle[row][col]
        return self.memo[(row, col)]

class Solution2:
    # Dynamic Programming: Bottom-Up
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        belowRow = triangle[-1]
        n = len(triangle)
        for r in range(n-2, -1, -1):
            curRow = []
            for c in range(r+1):
                smallestBelow = min(belowRow[c], belowRow[c+1])
                curRow.append(triangle[r][c]+smallestBelow)
            belowRow = curRow
        return belowRow[0]