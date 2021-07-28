## 1610. Maximum Number of Visible Points

### Description
Leetcode Link: [https://leetcode.com/problems/maximum-number-of-visible-points/]  
You are given an array points, an integer angle, and your location, where location = [posx, posy] and points[i] = [xi, yi] both denote integral coordinates on the X-Y plane.

Initially, you are facing directly east from your position. You cannot move from your position, but you can rotate. In other words, posx and posy cannot be changed. Your field of view in degrees is represented by angle, determining how wide you can see from any given view direction. Let d be the amount in degrees that you rotate counterclockwise. Then, your field of view is the inclusive range of angles [d - angle/2, d + angle/2].

Example 1:  
Input: points = [[2,1],[2,2],[3,3]], angle = 90, location = [1,1]  
Output: 3  
Explanation: The shaded region represents your field of view. All points can be made visible in your field of view, including [3,3] even though [2,2] is in front and in the same line of sight.  

Example 2:
Input: points = [[2,1],[2,2],[3,4],[1,1]], angle = 90, location = [1,1]
Output: 4
Explanation: All points can be made visible in your field of view, including the one at your location.

### Solution
* **Sliding Window**
1. Calculate the angle of each point respect to the location.
2. Sort the angle array.
3. Since it's a circle, we may end up overlapping view. Therefore, append the angle array again.
4. Use Sliding Window algorithm to find the answer.

```python
class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        sameLocation = 0
        arr_radian = []
        for x, y in points:
            if x == location[0] and y == location[1]:
                sameLocation += 1
                continue
            arr_radian.append(math.atan2(y-location[1], x-location[0]))
        
        arr_radian.sort()
        arr_radian = arr_radian + [x+2*math.pi for x in arr_radian]
        
        angle_in_radian = math.pi * angle/180
        
        visiblePoints = 0
        l = 0
        for r in range(len(arr_radian)):
            while arr_radian[r] - arr_radian[l] > angle_in_radian:
                l += 1
            visiblePoints = max(visiblePoints, r-l+1)
            
        return visiblePoints + sameLocation
```