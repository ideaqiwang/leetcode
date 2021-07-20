'''
44. Wildcard Matching

Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Example 1:
Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:
Input: s = "aa", p = "*"
Output: true
Explanation: '*' matches any sequence.

Example 3:
Input: s = "cb", p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.

Example 4:
Input: s = "adceb", p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".

Example 5:
Input: s = "acdcb", p = "a*c?b"
Output: false
'''

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        
        if p == s or p == "*":
            return True
        # dp[i][j] means if s[:i] matches p[:j]
        dp = [ [False] * (n+1) for _ in range(m+1)]
        dp[0][0] = True
        for j in range(1, n+1):
            dp[0][j] = dp[0][j-1] and p[j-1] == "*"
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if p[j-1] == "*":
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
                else: # p[j-1]=="?" or a letter
                    dp[i][j] = dp[i-1][j-1] and (s[i-1]==p[j-1] or p[j-1]=="?")
        return dp[m][n]
