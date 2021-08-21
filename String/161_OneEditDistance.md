## 161. One Edit Distance

### Description
Given two strings s and t, return true if they are both one edit distance apart, otherwise return false.

A string s is said to be one distance apart from a string t if you can:

Insert exactly one character into s to get t.  
Delete exactly one character from s to get t.  
Replace exactly one character of s with a different character to get t.  
 

Example 1:  
Input: s = "ab", t = "acb"  
Output: true  
Explanation: We can insert 'c' into s to get t.  

### Solution
* Time Complexity: O(n)

```python
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        ls, lt = len(s), len(t)
        # Ensure s is shorter than s
        if ls > lt:
            return self.isOneEditDistance(t, s)
        
        if lt - ls > 1:
            return False
        
        for i in range(ls):
            if s[i] != t[i]:
                if ls == lt:
                    return s[i+1:] == t[i+1:]
                # s and t have different lengths
                return s[i:] == t[i+1:]
        return ls + 1 == lt
```
