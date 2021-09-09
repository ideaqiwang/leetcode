## 296. Best Meeting Point

### Description
Given an m x n binary grid grid where each 1 marks the home of one friend, return the minimal total travel distance.

The total travel distance is the sum of the distances between the houses of the friends and the meeting point.

The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

Example 1:  
Input: grid = [[1,0,0,0,1],[0,0,0,0,0],[0,0,1,0,0]]  
Output: 6  
Explanation: Given three friends living at (0,0), (0,4), and (2,2).  
The point (0,2) is an ideal meeting point, as the total travel distance of 2 + 2 + 2 = 6 is minimal.
So return 6.

### Solution
* First we collect both the row and column coordinates, sort them and select their middle elements.
* Then we calculate the total distance as the sum of two independent 1D problems.

```python
class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        rows, cols = [], []
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    rows.append(i)
                    cols.append(j)
        rows.sort()
        cols.sort()
        
        mid = len(rows)//2
        x, y = rows[mid], cols[mid]
        
        distance = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    distance += abs(i-x) + abs(j-y)
        return distance
```
