## 1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit

### Description

Given an array of integers nums and an integer limit, return the size of the longest non-empty subarray such that the absolute difference between any two elements of this subarray is less than or equal to limit.

Example 1:  
Input: nums = [8,2,4,7], limit = 4  
Output: 2  
Explanation: All subarrays are:  
[8] with maximum absolute diff |8-8| = 0 <= 4.  
[8,2] with maximum absolute diff |8-2| = 6 > 4.   
[8,2,4] with maximum absolute diff |8-2| = 6 > 4.  
[8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.  
[2] with maximum absolute diff |2-2| = 0 <= 4.  
[2,4] with maximum absolute diff |2-4| = 2 <= 4.  
[2,4,7] with maximum absolute diff |2-7| = 5 > 4.  
[4] with maximum absolute diff |4-4| = 0 <= 4.  
[4,7] with maximum absolute diff |4-7| = 3 <= 4.  
[7] with maximum absolute diff |7-7| = 0 <= 4.   
Therefore, the size of the longest subarray is 2.  

Example 2:  
Input: nums = [10,1,2,4,7,2], limit = 5  
Output: 4  
Explanation: The subarray [2,4,7,2] is the longest since the maximum absolute diff is |2-7| = 5 <= 5.

### Solution
* Sliding Window
* Time Complexity: O(n)

1. Use two deques to store max and min values
2. Keep max deque decreasing and min deque increasing
3. Pop invalid values when scan the array

```python
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        
        maxq, minq = deque(), deque()
        l = 0
        for r in range(n):
            # Keep maxq decreasing
            while maxq and nums[r] > maxq[-1]:
                maxq.pop()
            # Keep minq increasing
            while minq and nums[r] < minq[-1]:
                minq.pop()

            maxq.append(nums[r])
            minq.append(nums[r])
            
            if maxq[0] - minq[0] > limit:
                if maxq[0] == nums[l]:
                    maxq.popleft()
                if minq[0] == nums[l]:
                    minq.popleft()
                l += 1
        return n - l
```