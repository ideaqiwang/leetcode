## 305. Number of Islands II
### Description
ou are given an empty 2D binary grid grid of size m x n. The grid represents a map where 0's represent water and 1's represent land. Initially, all the cells of grid are water cells (i.e., all the cells are 0's).

We may perform an add land operation which turns the water at position into a land. You are given an array positions where positions[i] = [ri, ci] is the position (ri, ci) at which we should operate the ith operation.

Return an array of integers answer where answer[i] is the number of islands after turning the cell (ri, ci) into a land.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:  
Input: m = 3, n = 3, positions = [[0,0],[0,1],[1,2],[2,1]]  
Output: [1,1,2,3]  
Explanation:  
Initially, the 2d grid is filled with water.  
- Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land. We have 1 island.  
- Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land. We still have 1 island.  
- Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land. We have 2 islands.  
- Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land. We have 3 islands.  

### Solution
* Union Find
* Time Complexity: O(n)

```python
Directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n+1)]
        self.rank = [0] * (n+1)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[px] = py
            self.rank[py] += 1
        return True
            
class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        def getIdx(x, y):
            return x*n+y

        uf = UnionFind(m*n)
        visited = set()
        res = []
        count = 0
        for x, y in positions:
            if (x, y) not in visited:
                count += 1
                idx = getIdx(x, y)
                for dx, dy in Directions:
                    nx, ny = x+dx, y+dy
                    if 0<=nx<m and 0<=ny<n and (nx, ny) in visited:
                        if uf.union(idx, getIdx(nx, ny)):
                            count -= 1
                visited.add((x, y))
            res.append(count)
        return res
```
