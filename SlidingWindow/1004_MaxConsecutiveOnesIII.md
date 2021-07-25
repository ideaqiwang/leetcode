## 1004. Max Consecutive Ones III

### Description
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

Example 1:  
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2  
Output: 6  
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.  

Example 2:  
Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3  
Output: 10  
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.  

### Solution

Use **Sliding Window** algorithm.
1. Initialize L and R index to 0.
2. Outer loop to move R index to right.
3. Update inventory given the constraint.
4. When it breaks the constraint, move L to left and update inventory.
5. Save the optimized length

#### Solution 1
Time Complexity: O(n)
```Python
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        longest = 0
        l = 0
        changed = 0
        for r in range(n):
            if nums[r] == 0:
                changed += 1
            while changed > k and l < n:
                if nums[l] == 0:
                    changed -= 1
                l += 1
            longest = max(longest, r-l+1)
        return longest
```

#### Solution 2
Instead of move L by one step in **Solution 1**, we could use a queue to save index of 0.
Move L to next element of the index of 0.  
Time Complexity:O(n)
```Python
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        indexOf0 = deque()
        longest = 0
        l = 0
        for r in range(n):
            if nums[r] == 0:
                indexOf0.append(r)
                k -= 1
            while k < 0:
                l = indexOf0.popleft()+1
                k += 1
            longest = max(longest, r-l+1)
        return longest
```
