## 76. Minimum Window Substring

### Description
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.

Example 1:  
Input: s = "ADOBECODEBANC", t = "ABC"  
Output: "BANC"  
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.  

Example 2:  
Input: s = "a", t = "a"  
Output: "a"  
Explanation: The entire string s is the minimum window.  

Example 3:  
Input: s = "a", t = "aa"  
Output: ""  
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.  

### Solution
Use **Sliding Window** algorithm
1. Create dictT which stores the count of each character
2. Initialize L, R to 0
3. Outer loop to move R to right
4. If s[r] is in t and the count of s[r] in window equals to the count in dictT, increase matched.
5. If the window matches t, update min length and start index. And move L to right in the inner loop

```python
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dictT = defaultdict(int)
        for c in t:
            dictT[c] += 1
        
        subL, subLen = 0, sys.maxsize
        window = defaultdict(int)
        matched = 0

        l = 0
        for r in range(len(s)):
            c_s = s[r]
            window[c_s] += 1
            
            if c_s in dictT and window[c_s] == dictT[c_s]:
                matched += 1
            
            while l <= r and matched == len(dictT):
                windowLen = r - l + 1
                if windowLen < subLen:
                    subLen = windowLen
                    subL = l
                window[s[l]] -= 1
                if s[l] in dictT and window[s[l]] < dictT[s[l]]:
                    matched -= 1
                l += 1
        return "" if subLen==sys.maxsize else s[subL:subL+subLen]
```