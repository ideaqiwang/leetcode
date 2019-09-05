'''
  Problem description: https://leetcode.com/problems/minimum-height-trees/
'''

class Solution:
  def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
    if n == 1:
      return [0]
    
    adj = [set() for x in range(n)]
    for p, q in edges:
      adj[p].add(q)
      adj[q].add(p)
    
    leaves = [i for i in range(n) if len(adj(i)) == 1]
    
    while n > 2:
      n -= len(leaves);
      newLeaves = []
      for leaf in leaves:
        otherNode = adj[leaf].pop()
        adj[otherNode].remove(leaf)
        if len(adj[otherNode]) == 1:
          newLeaves.append(otherNode)
      leaves = newLeaves
    return leaves
      
