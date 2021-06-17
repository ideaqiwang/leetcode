'''
261. Graph Valid Tree

You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.
Return true if the edges of the given graph make up a valid tree, and false otherwise.

Example 1:
   0
 / | \
1  2  3
|
4
Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true

Example 2:
0 - 1 - 2
    | \ |
    4   3
Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
Output: false
'''

class Solution:
    '''
    For a grpah of n nodes to be a valid tree, it mush meets the following:
    1. There're n-1 edges
    2. The graph is fully connected.
    '''
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        
        graph = [ [] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        q = deque([0])
        visited = set([0])
        while q:
            node = q.popleft()
            for neighbor in graph[node]:
                if neighbor in visited:
                    continue
                q.append(neighbor)
                visited.add(neighbor)

        return len(visited) == n
