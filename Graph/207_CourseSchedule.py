'''
207. Course Schedule

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

Example 2:
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
'''

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        
        graph = [[] for _ in range(numCourses)]
        indegrees = [0] * numCourses
        
        for child, parent in prerequisites:
            graph[parent].append(child)
            indegrees[child] += 1
        
        startNodes = [ i for i, degree in enumerate(indegrees) if degree == 0]
        q = deque(startNodes)
        
        while q:
            node = q.popleft()
            for child in graph[node]:
                indegrees[child] -= 1
                if indegrees[child] == 0:
                    q.append(child)
        return indegrees.count(0) == numCourses