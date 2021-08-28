## 695. Max Area of Island

### Description

You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

Example 1:
```
1 1 0 0 0
1 1 0 0 0
0 0 0 1 1
0 0 0 1 1
```
Input: [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
Output: 4

### Solution
* BFS

```python
DIRECTIONS = [(0, -1), (0, 1), (-1, 0), (1, 0)]

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        maxArea = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, self.bfs(grid, i, j, m, n))
        return maxArea

    def bfs(self, grid, i, j, m, n):
        q = deque([(i, j)])
        grid[i][j] = 0
        area = 0
        while q:
            x, y = q.popleft()
            area += 1
            for dx, dy in DIRECTIONS:
                nx, ny = x+dx, y+dy
                if 0<=nx<m and 0<=ny<n and grid[nx][ny] == 1:
                    q.append((nx, ny))
                    grid[nx][ny] = 0
        return area
```
