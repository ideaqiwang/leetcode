## 480. Sliding Window Median

### Description

The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle values.

For examples, if arr = [2,3,4], the median is 3.  
For examples, if arr = [1,2,3,4], the median is (2 + 3) / 2 = 2.5.  
You are given an integer array nums and an integer k. There is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the median array for each window in the original array. Answers within 10-5 of the actual value will be accepted.

Example 1:  
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3  
Output: [1.00000,-1.00000,-1.00000,3.00000,5.00000,6.00000]  
Explanation:  
Window position                Median  
---------------                -----  
[1  3  -1] -3  5  3  6  7        1  
 1 [3  -1  -3] 5  3  6  7       -1  
 1  3 [-1  -3  5] 3  6  7       -1  
 1  3  -1 [-3  5  3] 6  7        3  
 1  3  -1  -3 [5  3  6] 7        5  
 1  3  -1  -3  5 [3  6  7]       6  

Example 2:  
Input: nums = [1,2,3,4,2,3,1,4,2], k = 3  
Output: [2.00000,3.00000,3.00000,3.00000,2.00000,3.00000,2.00000]  

### Solution
* **Sliding Window** and **Two Heaps**

```python
class MedianFinder:
    def __init__(self):
        self.small = [] # max heap
        self.large = [] # min heap
    
    def add(self, num):
        heapq.heappush(self.large, num)
        heapq.heappush(self.small, -heapq.heappop(self.large))

        if len(self.small) > len(self.large):
            heapq.heappush(self.large, -heapq.heappop(self.small))

    def median(self):
        if len(self.large) > len(self.small):
            return self.large[0]
        return (self.large[0]-self.small[0]) / 2
    
    def remove(self, num):
        if num >= self.large[0]:
            self._rm(self.large, num)
        else:
            self._rm(self.small, -num)
    
    def _rm(self, heap, num):
        idx = heap.index(num)
        heap[idx] = heap[-1]
        heap.pop()
        heapify(heap)
        

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        n = len(nums)
        medians = []
        
        medianFinder = MedianFinder()
        l = 0
        for r in range(n):
            medianFinder.add(nums[r])
            if r >= k-1:
                medians.append(medianFinder.median())
                medianFinder.remove(nums[l])
                l += 1
        return medians
```