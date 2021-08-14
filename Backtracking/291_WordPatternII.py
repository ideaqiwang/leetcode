'''
291. Word Pattern II

Given a pattern and a string s, return true if s matches the pattern.

A string s matches a pattern if there is some bijective mapping of single characters to strings such that if each character in pattern is replaced by the string it maps to, then the resulting string is s. A bijective mapping means that no two characters map to the same string, and no character maps to two different strings.

Example 1:
Input: pattern = "abab", s = "redblueredblue"
Output: true
Explanation: One possible mapping is as follows:
'a' -> "red"
'b' -> "blue"

Example 2:
Input: pattern = "aaaa", s = "asdasdasdasd"
Output: true
Explanation: One possible mapping is as follows:
'a' -> "asd"
'''

class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        return self.isMatched(pattern, s, {}, set())
        
        
    def isMatched(self, pattern, s, char2word, used):
        if not pattern:
            return not s
        
        char = pattern[0]
        if char in char2word:
            word = char2word[char]
            if not s.startswith(word):
                return False
            return self.isMatched(pattern[1:], s[len(word):], char2word, used)
        
        # char not in char2word
        for i in range(len(s)):
            word = s[:i+1]
            if word in used:
                continue

            char2word[char] = word
            used.add(word)
            
            if self.isMatched(pattern[1:], s[i+1:], char2word, used):
                return True
            
            del char2word[char]
            used.remove(word)

        return False
