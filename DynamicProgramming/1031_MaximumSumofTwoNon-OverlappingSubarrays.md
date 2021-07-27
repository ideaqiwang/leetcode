## 1031. Maximum Sum of Two Non-Overlapping Subarrays

### Description
Given an array nums of non-negative integers, return the maximum sum of elements in two non-overlapping (contiguous) subarrays, which have lengths firstLen and secondLen.  (For clarification, the firstLen-length subarray could occur before or after the secondLen-length subarray.)

Formally, return the largest V for which V = (nums[i] + nums[i+1] + ... + nums[i+firstLen-1]) + (nums[j] + nums[j+1] + ... + nums[j+secondLen-1]) and either:

0 <= i < i + firstLen - 1 < j < j + secondLen - 1 < nums.length, or
0 <= j < j + secondLen - 1 < i < i + firstLen - 1 < nums.length.

Example 1:  
Input: nums = [0,6,5,2,2,5,1,9,4], firstLen = 1, secondLen = 2  
Output: 20  
Explanation: One choice of subarrays is [9] with length 1, and [6,5] with length 2.  

Example 2:  
Input: nums = [3,8,1,3,2,1,8,9,0], firstLen = 3, secondLen = 2  
Output: 29  
Explanation: One choice of subarrays is [3,8,1] with length 3, and [8,9] with length 2.  

### Solution
**Dynamic Programming**
* Case 1: The **first** subarray is before the **second** subarray.  
|    maxFirst    | maxSecond | i ...  
     ========      =========
* Case 2: The **second** subarray is before the **first** subarray.  
|    maxSecond    | maxFirst | i ...  
     =========      ========
* Time Complexity: O(n)
```python
class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        if not nums:
            return 0
        n = len(nums)
        prefixSum = [nums[0]] * n
        for i in range(1, n):
            prefixSum[i] = prefixSum[i-1] + nums[i]
    
        res = prefixSum[firstLen+secondLen-1]
        maxFirst = prefixSum[firstLen-1]
        maxSecond = prefixSum[secondLen-1]
        
        for i in range(firstLen+secondLen, n):
            maxFirst = max(maxFirst, prefixSum[i-secondLen]-prefixSum[i-secondLen-firstLen])
            maxSecond = max(maxSecond, prefixSum[i-firstLen]-prefixSum[i-firstLen-secondLen])
            res = max(res, maxFirst+prefixSum[i]-prefixSum[i-secondLen], maxSecond+prefixSum[i]-prefixSum[i-firstLen])
        return res
```
