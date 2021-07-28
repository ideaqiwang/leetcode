## 862. Shortest Subarray with Sum at Least K

### Description
Given an integer array nums and an integer k, return the length of the shortest non-empty subarray of nums with a sum of at least k. If there is no such subarray, return -1.

A subarray is a contiguous part of an array.

Example 1:  
Input: nums = [[84,-37,32,40,95], k = 167  
Output: 3  

Example 2:  
Input: nums = [1,2], k = 4  
Output: -1  

Example 3:  
Input: nums = [2,-1,2], k = 3  
Output: 3  

### Solution
* **Prefix Sum** and **Mono Queue**
1. Calculate prefix sum
2. Monoq keeps all values are increasing
```python
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefixSum = [0] * (n+1)
        for i in range(n):
            prefixSum[i+1] = prefixSum[i] + nums[i]
        
        minLength = sys.maxsize
        monoq = deque()
        for i, preSum_i in enumerate(prefixSum):
            while monoq and prefixSum[monoq[-1]] >= preSum_i:
                monoq.pop()
                
            while monoq and preSum_i-prefixSum[monoq[0]] >= k:
                minLength = min(minLength, i-monoq.popleft())
            
            monoq.append(i)
    
        return -1 if minLength == sys.maxsize else minLength
```