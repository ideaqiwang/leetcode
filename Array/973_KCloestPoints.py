'''
973. K Closest Points to Origin

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

Example 1:
Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
'''

class Solution1:
    # Use a Max Heap to store (distance, x, y)
    # Time Complexity: O(nlogk)
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # max heap
        heap = []
        for point in points:
            heapq.heappush(heap, (-self.distance(point), point[0], point[1]))
            if len(heap) > k:
                heapq.heappop(heap)
        return [ [item[1], item[2]] for item in heap ]
        
    def distance(self, p):
        return sqrt(p[0]*p[0] + p[1]*p[1])


class Solution2:
    # Quick Select
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [(self.distance(point), index) for index, point in enumerate(points)]
        self.quickSelect(distances, 0, len(points)-1, k)
        return [points[distances[i][1]] for i in range(k)]
    
    def quickSelect(self, distances, start, end, k):
        if start == end:
            return
    
        l, r = start, end
        m = (l+r) // 2
        pivot = distances[m]
        while l <= r:
            while l<=r and distances[l] < pivot:
                l += 1
            while l<=r and distances[r] > pivot:
                r -= 1
            if l <= r:
                distances[l], distances[r] = distances[r], distances[l]
                l += 1
                r -= 1
        if start<=r and r >= k:
            self.quickSelect(distances, start, r, k)
        elif l<=end and l <= k:
            self.quickSelect(distances, l, end, k)
                
    def distance(self, p):
        return sqrt(p[0]*p[0] + p[1]*p[1])


