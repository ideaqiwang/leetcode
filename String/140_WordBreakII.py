'''
140. Word Break II

Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:
Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]

Example 2:
Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
Explanation: Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: []
'''

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        return self.dfs(s, set(wordDict), {})
        
    def dfs(self, s, wordSet, memo):
        if s in memo:
            return memo[s]
        if not s:
            return []
        
        partitions = []

        for i in range(1, len(s)):
            prefix = s[:i]
            if prefix not in wordSet:
                continue

            subPartitions = self.dfs(s[i:], wordSet, memo)
            for partition in subPartitions:
                partitions.append(prefix+" "+partition)
        
        if s in wordSet:
            partitions.append(s)

        memo[s] = partitions
        return partitions
