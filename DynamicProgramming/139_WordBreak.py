'''
139. Word Break

Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
'''

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        
        n = len(s)
        # dp[l] refers to if substring s[:l] can be broke into words
        # i seperate the substring into two smaller substrings s[:i] and s[i+1, l]
        dp = [False] * (n+1)
        dp[0] = True
        
        for l in range(1, n+1):
            for i in range(l):
                if dp[i] and s[i:l] in wordSet:
                    dp[l] = True
                    break
        return dp[n]
