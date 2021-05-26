'''
118. Pascal's Triangle

Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

1
1 1
1 2 1
1 3 3 1
1 4 6 4 1

Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:
Input: numRows = 1
Output: [[1]]
'''

class Solution:
    '''
    Solution 1:
    Dynamic Programming:
    Use the previous row to calculate the next row.
    '''
    def generate(self, numRows):
        triangles = []
        for r in range(numRows):
            row = [1] * (r+1)
            for i in range(1, r):
                row[i] = triangles[-1][i-1] + triangles[-1][i]
            triangles.append(row)
        return triangles
    
    '''
    Solution 2:
    DFS
    '''
    def dfs(self, rowNum, triangles):
        if rowNum == 0:
            return
        self.dfs(rowNum-1, triangles)

        row = [1] * rowNum
        for i in range(1, rowNum-1):
            row[i] = triangles[-1][i-1] + triangles[-1][i]
        triangles.append(row)
    
    def generate2(self, numRows):
        triangles = []
        self.dfs(numRows, triangles)
        return triangles