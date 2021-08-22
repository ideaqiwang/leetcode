## 317. Shortest Distance From All Buildings

### Description
You are given an m x n grid grid of values 0, 1, or 2, where:

each 0 marks an empty land that you can pass by freely,  
each 1 marks a building that you cannot pass through, and  
each 2 marks an obstacle that you cannot pass through.  
You want to build a house on an empty land that reaches all buildings in the shortest total travel distance. You can only move up, down, left, and right.  

Return the shortest travel distance for such a house. If it is not possible to build such a house according to the above rules, return -1.

The total travel distance is the sum of the distances between the houses of the friends and the meeting point.

The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

Exmaple 1:  
Input: grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]  
Output: 7  
Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2).  
The point (1,2) is an ideal empty land to build a house, as the total travel distance of 3+3+1=7 is minimal. So return 7.

### Solution
* Do BSF traversal from grid[i][j] == 1. When buildings are less than empty lands, this approach saves time.  
* Time Complexity: O(M^2 * n^2), M is the number of rows, N is the number of columns.

```python
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        self.distance = [[0] * n for _ in range(m)]
        self.reachable_count = [[0] * n for _ in range(m)]

        shortest, houses = sys.maxsize, 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.bfs(grid, i, j)
                    houses += 1
        
        for i in range(m):
            for j in range(n):
                if self.reachable_count[i][j] == houses:
                    shortest = min(shortest, self.distance[i][j])
        return shortest if shortest != sys.maxsize else -1

    def bfs(self, grid, i, j):
        visited = set([(i,j)])
        q = deque([(i, j, 0)])
        while q:
            x, y, dist = q.popleft()
            self.distance[x][y] += dist
            
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_x, new_y = x+dx, y+dy
                if self.isValid(grid, new_x, new_y, visited):
                    visited.add((new_x, new_y))
                    if grid[new_x][new_y] == 0:
                        q.append((new_x, new_y, dist+1))
                        self.reachable_count[new_x][new_y] += 1

    def isValid(self, grid, x, y, visited):
        if not (0 <= x < len(grid)) or not (0 <= y < len(grid[0])):
            return False
        return (x, y) not in visited
```
