'''
444. Sequence Reconstruction

Check whether the original sequence org can be uniquely reconstructed from the sequences in seqs.
The org sequence is a permutation of the integers from 1 to n, with 1 ≤ n ≤ 104.
Reconstruction means building a shortest common supersequence of the sequences in seqs
(i.e., a shortest sequence so that all sequences in seqs are subsequences of it).
Determine whether there is only one sequence that can be reconstructed from seqs and it is the org sequence.

Example 1:
Input: org = [1,2,3], seqs = [[1,2],[1,3]]
Output: false
Explanation: [1,2,3] is not the only one sequence that can be reconstructed, because [1,3,2] is also a valid sequence that can be reconstructed.

Example 2:
Input: org = [1,2,3], seqs = [[1,2]]
Output: false
Explanation: The reconstructed sequence can only be [1,2].

Example 3:
Input: org = [1,2,3], seqs = [[1,2],[1,3],[2,3]]
Output: true
Explanation: The sequences [1,2], [1,3], and [2,3] can uniquely reconstruct the original sequence [1,2,3].

Example 4:
Input: org = [4,1,5,2,6,3], seqs = [[5,2,6,3],[4,1,5,2]]
Output: true
'''

class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        
        def buildGraph(seqs):
            graph = {}
            for seq in seqs:
                for node in seq:
                    if node not in graph:
                        graph[node] = set()
            for seq in seqs:
                for i in range(len(seq)-1):
                    graph[seq[i]].add(seq[i+1])
            return graph
        
        def getIndegree(graph):
            indegree = { node: 0 for node in graph }
            for node in graph:
                for neighbor in graph[node]:
                    indegree[neighbor] += 1
            return indegree
        
        graph = buildGraph(seqs)
        indegree = getIndegree(graph)
        
        if len(indegree) != len(org):
            return False
        
        startNodes = [ node for node in indegree if indegree[node] == 0 ]
  
        output = []
        q = deque(startNodes)
        visited = set(startNodes)
        while q:
            if len(q) > 1:
                return False
            node = q.popleft()
            output.append(node)
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        return output == org
