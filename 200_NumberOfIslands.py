'''
@Description https://leetcode.com/problems/number-of-islands/

'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        visited = set() # Record all positions that are already in queue
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += 1
                    self.bfs(grid, i, j, visited)
        return count
                
        
    def bfs(self, grid, i, j, visited):
        q = collections.deque([(i, j)])
        visited.add((i, j))
        while q:
            r, c = q.popleft()
            grid[r][c] = "0"
            for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                if self.isValid(grid, nr, nc) and (nr, nc) not in visited:
                    q.append((nr, nc))
                    visited.add((nr, nc))
    
    def isValid(self, grid, r, c):
        return 0<=r<len(grid) and 0<=c<len(grid[0]) and grid[r][c] == "1"
