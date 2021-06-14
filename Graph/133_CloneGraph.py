'''
133. Clone Graph

Given a reference of a node in a connected undirected graph.
Return a deep copy (clone) of the graph.
Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    # DFS
    def __init__(self):
        self.visited = {}
    
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        if node in self.visited:
            return self.visited[node]
        clone_node = Node(node.val, [])
        self.visited[node] = clone_node
        
        for neighbor in node.neighbors:
            clone_node.neighbors.append(self.cloneGraph(neighbor))    
        return clone_node
    
    # BSF
    def cloneGraph2(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        visited = { node: Node(node.val, []) }
        q = deque([node])
        
        while q:
            n = q.popleft()
            for neighbor in n.neighbors:
                if neighbor not in visited:
                    q.append(neighbor)
                    visited[neighbor] = Node(neighbor.val, [])
                visited[n].neighbors.append(visited[neighbor])
        return visited[node]
                
                