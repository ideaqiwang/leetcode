## 5. Longest Palindromic Substring
### Desription
Given a string s, return the longest palindromic substring in s.

Example 1:  
Input: s = "babad"  
Output: "bab"  
Note: "aba" is also a valid answer.  

Example 2:  
Input: s = "cbbd"  
Output: "bb"  

Example 3:  
Input: s = "ac"  
Output: "a"  

### Solution
### - Expand Around Center
* Time Complexity: O(n^2)
```python
class Solution:
    # Use two pointers to search the longest palidromic substring from middle position to left and right.
    start = 0 # The start index of the longest palindromic substring 
    end = 0   # The end index of the longest palindromic substring

    def longestPalindrome(self, s: str) -> str:
        # Loop through each index of the given string s.
        # For each index, it would be treated as the middle postion.
        # Then expand the palindromic substring. 
        for i in range(len(s)):
          self.findLongest(s, i, i)    # Then length of a palindromic string can be even or odd.
          self.findLongest(s, i, i+1)  # Therefore, we need to search both positions for each index.
        return s[self.start:self.end+1]
        
    def findLongest(self, s, l, r):
      while l>=0 and r<len(s) and s[l]==s[r]:
        l -= 1
        r += 1
      # Compare the current longest palindromic string with the current substring
      # r-l-2 is because l and r would be outside of the found palindromic string
      if (self.end-self.start) < (r-l-2):
        self.start = l+1
        self.end = r-1
```

#### - DP
* Time Complexity: O(n^2)

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return s
        
        n = len(s)
        # dp[l][r] means if s[l:r+1] is a palindrome
        # dp[l][r] = dp[l+1][r-1] and s[l] == s[r]
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        
        start, length = 0, 1
        
        for l in range(n-1, -1, -1):
            for r in range(l+1, n):
                if s[l] != s[r]:
                    continue
            
                if r-l == 1 or dp[l+1][r-1]:
                    dp[l][r] = True
                    if r-l+1 > length:
                        length = r-l+1
                        start = l
  
        return s[start: start+length]
```
