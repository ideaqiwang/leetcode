'''
@Desciption https://leetcode.com/problems/course-schedule-ii/
@IDEA 
  Topological sort
  The idea is same as Course Schedule. 
'''

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        indegrees = [0] * numCourses
        
        for child, parent in prerequisites:
          graph[parent].append(child)
          indegrees[child] += 1
        
        q = collections.deque()
        for node in range(numCourses):
          if indegrees[node] == 0:
            q.append(node)
        
        order = []
        while q:
          node = q.popleft()
          order.append(node)
          for neighbor in graph[node]:
            indegrees[neighbor] -= 1
            if indegrees[neighbor] == 0:
              q.append(neighbor)
        return order if len(order)==numCourses else []
