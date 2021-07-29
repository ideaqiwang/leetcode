## 1151. Minimum Swaps to Group All 1's Together

### Description
Given a binary array data, return the minimum number of swaps required to group all 1’s present in the array together in any place in the array.

Example 1:  
Input: data = [1,0,1,0,1]  
Output: 1  
Explanation:  
There are 3 ways to group all 1's together:  
[1,1,1,0,0] using 1 swap.  
[0,1,1,1,0] using 2 swaps.  
[0,0,1,1,1] using 1 swap.  
The minimum is 1.  

Example 2:  
Input: data = [0,0,0,1,0]  
Output: 0  
Explanation:   
Since there is only one 1 in the array, no swaps needed.  

### Solution
* **Sliding Window**
1. The number of 1 is the maximum swaps needed. Hence, it's the window size.
2. Use sliding window technique to find the minimum number of 0 in a window with the fixed size of the number of 1.

```python
class Solution:
    def minSwaps(self, data: List[int]) -> int:
        one_count = sum(data)
        if one_count == 0:
            return 0
        
        minSwaps = len(data)
        zero_count = 0
        l = 0
        for r in range(len(data)):
            if data[r] == 0:
                zero_count += 1
            if r+1 >= one_count:
                minSwaps = min(minSwaps, zero_count)
                if data[l] == 0:
                    zero_count -= 1
                l += 1
        return minSwaps
```