'''
378. Kth Smallest Element in a Sorted Matrix

Given an n x n matrix where each of the rows and columns are sorted in ascending order, return the kth smallest element in the matrix.
Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example 1:
Input: matrix = [[1, 5, 9 ],
                 [10,11,13],
                 [12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13

Example 2:
Input: matrix = [[-5]], k = 1
Output: -5
'''

class Solution:
    # Binary Search
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        
        start, end = matrix[0][0], matrix[n-1][n-1]
        while start < end:
            mid = (start + end) // 2
            count = self.countLessEqual(matrix, mid, start, end)
            if count < k:
                start = mid+1
            else:
                end = mid 
        return end
        
    def countLessEqual(self, matrix, mid, smaller, larger):
        count, n = 0, len(matrix)
        row, col = n-1, 0
        while row >= 0 and col < n:
            if matrix[row][col] > mid:
                row -= 1
            else:
                col += 1
                count += row+1
        return count
