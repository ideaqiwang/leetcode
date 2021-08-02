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
        dict1 = Counter(s1)
        window_dict = defaultdict(int)
        
        m, n = len(s1), len(s2)
        matched = 0
        for r in range(n):
            c_r = s2[r]
            window_dict[c_r] += 1
            if c_r in dict1 and dict1[c_r] == window_dict[c_r]:
                matched += 1
        
            if r+1 >= m:
                if matched == len(dict1):
                    return True
                l = r-m+1
                c_l = s2[l]
                window_dict[c_l] -= 1
                if window_dict[c_l] == 0:
                    del window_dict[c_l]
                    if c_l in dict1:
                        matched -= 1
                
        return False
```