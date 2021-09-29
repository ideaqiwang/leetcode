## 1235. Maximum Profit in Job Scheduling
### Description
We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].

You're given the startTime, endTime and profit arrays, return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.

If you choose a job that ends at time X you will be able to start another job that starts at time X.

Example 1:  
Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]  
Output: 120  
Explanation: The subset chosen is the first and fourth job.   
Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.  

### Solution

```python
import heapq
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(profit)
        intervals = [(startTime[i], endTime[i], profit[i]) for i in range(n)]
        intervals.sort()

        hp = []
        maxProfit = 0
        for start, end, profit in intervals:
            while hp and start >= hp[0][0]:
                maxProfit = max(maxProfit, hp[0][1])
                heapq.heappop(hp)
            heapq.heappush(hp, (end, profit+maxProfit))

        while hp:
            maxProfit = max(maxProfit, hp[0][1])
            heapq.heappop(hp)
        return maxProfit
```
