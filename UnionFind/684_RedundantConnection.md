## 684. Redundant Connection

### Description

In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

Example 1:  
```
 1 - - 2
 |   /
 | /
 3
```
Input: edges = [[1,2],[1,3],[2,3]]  
Output: [2,3]  

Example 2:  
```
2 -- 1 -- 5
|    |
3 -- 4
```
Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]  
Output: [1,4]  

### Solution
* Union Find
* Time Complexity: O(n)

```python
class UnionFind:
    def __init__(self, n):
        self.parents = [ i for i in range(n+1) ]
        self.ranks = [0] * (n+1)
    
    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, a, b):
        parent_a, parent_b = self.find(a), self.find(b)
        if parent_a == parent_b:
            return False
        if self.ranks[parent_a] < self.ranks[parent_b]:
            self.parents[parent_a] = parent_b
        elif self.ranks[parent_b] < self.ranks[parent_a]:
            self.parents[parent_b] = parent_a
        else:
            self.parents[parent_a] = parent_b
            self.ranks[parent_b] += 1
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges))
        for edge in edges:
            if not uf.union(*edge):
                return edge
        return []
```
