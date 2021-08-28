## 547. Number of Provinces

### Description
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

Example 1:
```
1 --- 2

   3
```
Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]  
Output: 2  

### Solution

#### - Solution 1: BSF
* Time Complexity: O(n^2)

```python
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        self.visited = set()
        count = 0
        for i in range(len(isConnected)):
            if i not in self.visited:
                self.bfs(isConnected, i)
                count += 1
        return count
    
    def bfs(self, grid, start):
        q = deque([start])
        self.visited.add(start)
        while q:
            node = q.popleft()
            for neighbor in range(len(grid)):
                if grid[node][neighbor] == 1 and neighbor not in self.visited:
                    q.append(neighbor)
                    self.visited.add(neighbor)
```

#### - Solution 2: Union Find
* Time Complexity: O(n^2)

```python
class UnionFind:
    def __init__(self, n):
        self.parents = [*range(n)]
        self.ranks = [0] * (n)
    
    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
    
        if self.ranks[px] < self.ranks[py]:
            self.parents[px] = py
        elif self.ranks[px] > self.ranks[py]:
            self.parents[py] = px
        else:
            self.parents[px] = py
            self.ranks[py] += 1
        return True

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        count = n = len(isConnected)
        uf = UnionFind(n*n)
        
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1 and i != j:
                    if uf.union(i, j):
                        count -= 1
        return count
```
