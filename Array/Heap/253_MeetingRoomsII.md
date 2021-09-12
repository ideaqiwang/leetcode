## 253. Meeting Rooms II
### Description
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

Example 1:  
Input: intervals = [[0,30],[5,10],[15,20]]  
Output: 2  
Example 2:  
Input: intervals = [[7,10],[2,4]]  
Output: 1  

### Solution

#### - Heap
* Time Complexity: O(nlog(n))

```python
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        rooms = [intervals[0][1]]

        for i in range(1, len(intervals)):
            if rooms[0] <= intervals[i][0]:
                heapq.heappop(rooms)
            
            heapq.heappush(rooms, intervals[i][1])
        return len(rooms)
```

#### - Line Sweep
* Time Complexity: O(nlog(n))

```python
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        points = []
        for start, end in intervals:
            points.append((start, 1))
            points.append((end, -1))
        points.sort()
        
        total, cur = 0, 0
        for _, x in points:
            cur += x
            total = max(total, cur)
        return total
```
