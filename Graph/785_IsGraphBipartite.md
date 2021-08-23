## 785. Is Graph Bipartite?

### Description

There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1. You are given a 2D array graph, where graph[u] is an array of nodes that node u is adjacent to. More formally, for each v in graph[u], there is an undirected edge between node u and node v. The graph has the following properties:

There are no self-edges (graph[u] does not contain u).  
There are no parallel edges (graph[u] does not contain duplicate values).  
If v is in graph[u], then u is in graph[v] (the graph is undirected).  
The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.  
A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.  

Return true if and only if it is bipartite.  

### Solution
* Travese the graph level by level and color each level with 1 and -1 in turn

```python
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        q = deque()
        color = {}
        for node in range(len(graph)):
            if node in color:
                continue
            q.append(node)
            color[node] = 1

            while q:
                node = q.popleft()
                for neighbor in graph[node]:
                    if neighbor not in color:
                        q.append(neighbor)
                        color[neighbor] = -color[node]
                    elif color[neighbor] != -color[node]:
                        return False
        return True
```
