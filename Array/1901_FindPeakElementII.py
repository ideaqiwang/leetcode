'''
1901. Find a Peak Element II

A peak element in a 2D grid is an element that is strictly greater than all of its adjacent neighbors to the left, right, top, and bottom.
Given a 0-indexed m x n matrix mat where no two adjacent cells are equal, find any peak element mat[i][j] and return the length 2 array [i,j].
You may assume that the entire matrix is surrounded by an outer perimeter with the value -1 in each cell.
You must write an algorithm that runs in O(m log(n)) or O(n log(m)) time.

Example 1:
Input: mat = [[10,20,15],[21,30,14],[7,16,32]]
Output: [1,1]
Explanation: Both 30 and 32 are peak elements so [1,1] and [2,2] are both acceptable answers.
'''

class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        l, r = 0, n-1
        while l <= r:
            mc = (l+r) // 2
            maxRow = 0
            for i in range(m):
                maxRow = i if mat[i][mc] > mat[maxRow][mc] else maxRow
            
            leftBig = (mc-1 >= l and mat[maxRow][mc-1] > mat[maxRow][mc])
            rightBig = (mc+1<= r and mat[maxRow][mc+1] > mat[maxRow][mc])
            if not leftBig and not rightBig:
                return [maxRow, mc]
            elif leftBig:
                r = mc - 1
            else:
                l = mc + 1