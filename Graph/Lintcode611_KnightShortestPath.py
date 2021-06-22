'''
@Description
Given a knight in a chessboard (a binary matrix with 0 as empty and 1 as barrier) with a source position, find the shortest path to a destination position, return the length of the route.
Return -1 if destination cannot be reached

@IDEA
  1. BSF to search the shortest path
  2. Records steps of each position with haspmap
'''

"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path 
    """
    def shortestPath(self, grid, source, destination):
        # write your code here
        if not grid:
            return -1
        
        distance = {(source.x, source.y) : 0}
        q = collections.deque([(source.x, source.y)])
        while q:
            curNode = q.popleft()
            if curNode==(destination.x, destination.y):
                return distance[curNode]
            for nextMove in self.nextMoves(curNode, grid):
                if nextMove not in distance:
                    q.append(nextMove)
                    distance[nextMove] = distance[curNode]+1
        return -1
                
                
    def nextMoves(self, node, grid):
        x, y = node[0], node[1]
        moves = []
        for dx, dy in [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]:
            newX, newY = x+dx, y+dy
            if 0<=newX<len(grid) and 0<=newY<len(grid[0]) and grid[newX][newY]==0:
                moves.append((newX, newY))
        return moves
