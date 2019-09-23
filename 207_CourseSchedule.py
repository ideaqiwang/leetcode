'''
@Description https://leetcode.com/problems/course-schedule/
@IDEA
  1. Build a directed graph based on the dependency direction.
  2. Calculate each node' indegree.
  3. Put all nodes with indegree 0 into queue.
  4. Pop nodes one by one and reduce indegree by one from its neighbors.
     If the updated indegreee is 0, put it into q.
'''

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        indegrees = [0] * numCourses
        
        # outNode depends on inNode so direction is outNode -> inNode
        for inNode, outNode in prerequisites: 
            graph[outNode].append(inNode)
            indegrees[inNode] += 1
        
        q = collections.deque()
        for node in range(numCourses):
            if indegrees[node] == 0:
                q.append(node)
        order = []
        while q:
            curNode = q.popleft()
            order.append(order)
            for neighbor in graph[curNode]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    q.append(neighbor)
        return len(order) == numCourses
