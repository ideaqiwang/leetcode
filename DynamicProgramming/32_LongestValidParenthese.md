## 32. Longest Valid Parentheses

### Description

Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:  
Input: s = "(()"  
Output: 2  
Explanation: The longest valid parentheses substring is "()".  

Example 2:  
Input: s = ")()())"  
Output: 4  
Explanation: The longest valid parentheses substring is "()()".  

### Solution
* DP

```python
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return 0
        # dp[i] means the longest valid parenthese starting with index i
        dp = [0] * n
        longest = 0
        
        for i in range(n-2, -1, -1):
            if s[i] == '(':
                j = i + dp[i+1] + 1
                if j < n and s[j] == ')':
                    dp[i] = dp[i+1] + 2
                    if j+1 < n:
                        dp[i] += dp[j+1]
                longest = max(longest, dp[i])
 
        return longest
```
