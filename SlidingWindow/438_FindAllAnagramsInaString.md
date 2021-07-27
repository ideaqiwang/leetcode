## 438. Find All Anagrams in a String

### Description
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

Example 1:  
Input: s = "cbaebabacd", p = "abc"  
Output: [0,6]  
Explanation:  
The substring with start index = 0 is "cba", which is an anagram of "abc".  
The substring with start index = 6 is "bac", which is an anagram of "abc".  

Example 2:  
Input: s = "abab", p = "ab"  
Output: [0,1,2]  
Explanation:  
The substring with start index = 0 is "ab", which is an anagram of "ab".  
The substring with start index = 1 is "ba", which is an anagram of "ab".  
The substring with start index = 2 is "ab", which is an anagram of "ab".  

### Solution
**Sliding Window**
* Time Complexity: O(n)
```python
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        char2count_p = defaultdict(int)
        for c in p:
            char2count_p[c] += 1
        
        char2count_s = defaultdict(int)
        res = []
        l = 0
        for r in range(len(s)):
            c_s = s[r]
            char2count_s[c_s] += 1
    
            if r+1 >= len(p):
                if char2count_s == char2count_p:
                    res.append(l)
                c_l = s[l]
                char2count_s[c_l] -= 1
                if char2count_s[c_l] == 0:
                    del char2count_s[c_l]
                
                l += 1
        return res
```
