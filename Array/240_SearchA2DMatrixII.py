'''
240. Search a 2D Matrix II

Write an efficient algorithm that searches for a target value in an m x n integer matrix. The matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.

Example 1:
1, 4, 7, 11, 15
2, 5, 8, 12, 19
3, 6, 9, 16, 22
10,13,14,17, 24
18,21,23,26, 30
Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
Output: true
'''

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        r, c = m-1, 0
        while r >= 0 and c < n:
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                r -= 1
            else:
                c += 1
        return False