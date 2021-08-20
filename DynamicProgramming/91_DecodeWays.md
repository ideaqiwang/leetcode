## 91. Decode Ways

### Description

A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

Example 1:  
Input: s = "12"  
Output: 2  
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).  

### Solution
* DP : dp[i] = dp[i-1] + dp[i-2]

```python
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        # dp[i] = dp[i-1] + dp[i-2]
        # dp[i] means the number of decoding ways of the first i characters - s[0, i-1]
        dp = [0] * (n+1)
        dp[0] = 1
        if s[0] != '0':
            dp[1] = 1
        
        for i in range(2, n+1):
            if s[i-1] != '0':
                dp[i] = dp[i-1]
    
            if (s[i-2] == '1') or (s[i-2] == '2' and s[i-1] <= '6'):
                dp[i] += dp[i-2]

        return dp[n]
```
