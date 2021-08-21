## 340. Longest Substring with At Most K Distinct Characters

### Description
Given a string s and an integer k, return the length of the longest substring of s that contains at most k distinct characters.

Example 1:  
Input: s = "eceba", k = 2  
Output: 3  
Explanation: The substring is "ece" with length 3.  

Example 2:  
Input: s = "aa", k = 1  
Output: 2  
Explanation: The substring is "aa" with length 2.  

### Solution

Use **Sliding Window** algorithm.

1. Initialize L, R to 0.
2. Move R to right in outer loop. Update character counter.
3. When there're more than k characters in window, move L to right in inner loop.
4. Update the optimized value.

```python
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0 or len(s) == 0:
            return 0

        window = defaultdict(int)
        l = 0
        longest = 0
        
        for r in range(len(s)):
            window[s[r]] += 1
            while l <= r and len(window) > k:
                window[s[l]] -= 1
                if window[s[l]] == 0:
                    del window[s[l]]
                l += 1

            longest = max(longest, r-l+1)
        return longest
```
