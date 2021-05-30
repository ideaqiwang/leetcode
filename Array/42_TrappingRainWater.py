'''
42. Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9


'''

class Solution:
    '''
    Dynamic Programming
    '''
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxFromLeft, maxFromRight = [0]*n, [0]*n
        hFromLeft = hFromRight = 0
        for i in range(n):
            hFromLeft = max(hFromLeft, height[i])
            hFromRight = max(hFromRight, height[n-i-1])
            maxFromLeft[i] = hFromLeft
            maxFromRight[n-i-1] = hFromRight
        total = 0
        for i in range(n):
           total += min(maxFromLeft[i], maxFromRight[i]) - height[i] 
        return total

    '''
    As long as right_max[i]>left_max[i], the water trapped depends upon the left_max,
    and similar is the case when left_max[i]>right_max[i].
    '''
    def trap2(self, height: List[int]) -> int:
        n = len(height)
        if n < 3:
            return 0
        leftMax, rightMax = height[0], height[-1]
        l, r = 0, n-1
        total = 0
        while l < r :
            if height[l] < height[r]:
                if height[l] >= leftMax:
                    leftMax = height[l]
                else:
                    total += leftMax - height[l]
                l += 1
            else:
                if height[r] >= rightMax:
                    rightMax = height[r]
                else:
                    total += rightMax - height[r]
                r -= 1
                
        return total