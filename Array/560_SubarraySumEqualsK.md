## 560. Subarray Sum Equals K

### Description
Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

Example 1:  
Input: nums = [1,1,1], k = 2  
Output: 2  

Example 2:  
Input: nums = [1,2,3], k = 3  
Output: 2  

### Solution

* sum[i,j] = prefixSum[0,j] - prefixSum[0,i]
* Time Complexity: O(n)

```python
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum2count = defaultdict(int)
        sum2count[0] = 1

        prefixSum = 0
        count = 0
        for i in range(len(nums)):
            prefixSum += nums[i]
            compliment = prefixSum-k
            if compliment in sum2count:
                count += sum2count[compliment]
            
            sum2count[prefixSum] += 1    
        return count
```
