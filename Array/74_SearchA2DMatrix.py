'''
74. Search a 2D Matrix

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.

Example 1:
1  3  5  7
10 11 16 20
23 30 34 60
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
'''

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        start, end = 0, m*n-1
        while start+1 < end:
            mid = (start+end) // 2
            if self.getValue(matrix, mid) > target:
                end = mid
            else:
                start = mid
        if self.getValue(matrix, start) == target or self.getValue(matrix, end) == target:
            return True
        return False
    
    def getValue(self, matrix, index):
        cols = len(matrix[0])
        r, c = index // cols, index % cols
        return matrix[r][c]