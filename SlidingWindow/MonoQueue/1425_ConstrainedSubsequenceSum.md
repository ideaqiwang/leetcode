## 1425. Constrained Subsequence Sum

### Description

Given an integer array nums and an integer k, return the maximum sum of a non-empty subsequence of that array such that for every two consecutive integers in the subsequence, nums[i] and nums[j], where i < j, the condition j - i <= k is satisfied.

A subsequence of an array is obtained by deleting some number of elements (can be zero) from the array, leaving the remaining elements in their original order.

Example 1:  
Input: nums = [10,2,-10,5,20], k = 2  
Output: 37  
Explanation: The subsequence is [10, 2, 5, 20].  

Example 2:  
Input: nums = [-1,-2,-3], k = 1  
Output: -1  
Explanation: The subsequence must be non-empty, so we choose the largest number.  

### Solution
* Sliding Window and Mono Queue
* Time Complexity: O(n)

```python
class Solution:
    '''
        dp[i] = max(0, dp[i - k], dp[i - k + 1], .., dp[i -1]) + A[i]
        dp[i] is the max sum we can have from A[:i] when A[i] has been chosen.
        q stores dp[i - k], dp[i-k+1], .., dp[i - 1] whose values are larger than 0 in a decreasing order
    '''
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        dp = list(nums)
        q = deque()
        
        for i in range(n):
            # deque[0] is the max of (0, dp[i - k], dp[i-k+1], .., dp[i - 1])
            dp[i] += q[0] if q else 0
            while q and dp[i] > q[-1]:
                q.pop()
            
            if dp[i] > 0:
                q.append(dp[i])
            
            if i >= k and q and dp[i-k] == q[0]:
                q.popleft()
        return max(dp)
```