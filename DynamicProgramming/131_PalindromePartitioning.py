'''
131. Palindrome Partitioning

Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.

Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:
Input: s = "a"
Output: [["a"]]
'''

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        return self.dfs(s, {})
    
    def dfs(self, s, memo):
        if not s:
            return []
        if s in memo:
            return memo[s]
        
        partitions = []
        for i in range(1, len(s)+1):
            prefix = s[:i]
            if not self.isPalindrome(prefix):
                continue
            
            subPartitions = self.dfs(s[i:], memo)
            for partition in subPartitions:
                partitions.append([prefix] + partition)
        
        if self.isPalindrome(s):
            partitions.append([s])
        memo[s] = partitions
        return partitions
        
        
    def isPalindrome(self, s):
        return s == s[::-1]
