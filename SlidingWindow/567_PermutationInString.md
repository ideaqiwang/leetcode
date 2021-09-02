## 567. Permutation in String

### Description

Given two strings s1 and s2, return true if s2 contains the permutation of s1.

In other words, one of s1's permutations is the substring of s2.

Example 1:  
Input: s1 = "ab", s2 = "eidbaooo"  
Output: true  
Explanation: s2 contains one permutation of s1 ("ba").  

Example 2:  
Input: s1 = "ab", s2 = "eidboaoo"  
Output: false  

### Solution
* **Sliding Window**
* Time Complexity: O(n)
1. Convert string to dict(char: counter)
2. Use Sliding Window technique to scan the whole string

```python
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dict1 = defaultdict(int)
        for c in s1:
            dict1[c] += 1
        window_dict = defaultdict(int)
        
        m, n = len(s1), len(s2)
        for r in range(n):
            window_dict[s2[r]] += 1
            
            if r+1 >= m:
                if dict1 == window_dict:
                    return True
                l = r-m+1
                window_dict[s2[l]] -= 1
                if window_dict[s2[l]] == 0:
                    del window_dict[s2[l]]
        return False
```
