## 304. Range Sum Query 2D - Immutable

### Description

Given a 2D matrix matrix, handle multiple queries of the following type:

Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
Implement the NumMatrix class:

NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Example 1:  
Input: ["NumMatrix","sumRegion","sumRegion","sumRegion"]  
       [[[[3,0,1],[5,6,3],[1,2,0]]],[1,1,2,2],[1,0,2,1],[0,1,1,2]]  
Output: [null,11,14,10]  

### Solution

```python
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        self.areaSum = [[0] * (n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                self.areaSum[i][j] = self.areaSum[i-1][j]+self.areaSum[i][j-1]+matrix[i-1][j-1]-self.areaSum[i-1][j-1]
 
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # area = areaSum[r2][c2]-areaSum[r1-1][c2]-areaSum[r2][c1-1]+areaSum[r1-1][c1-1]
        return self.areaSum[row2+1][col2+1] - self.areaSum[row1][col2+1] \
                - self.areaSum[row2+1][col1] + self.areaSum[row1][col1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
```
