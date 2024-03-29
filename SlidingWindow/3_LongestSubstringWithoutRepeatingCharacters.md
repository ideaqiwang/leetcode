## 3. Longest Substring Without Repeating Characters

### Description
Given a string s, find the length of the longest substring without repeating characters.

Example 1:  
Input: s = "abcabcbb"  
Output: 3  
Explanation: The answer is "abc", with the length of 3.  

Example 2:  
Input: s = "bbbbb"  
Output: 1  
Explanation: The answer is "b", with the length of 1.  

Example 3:  
Input: s = "pwwkew"  
Output: 3  
Explanation: The answer is "wke", with the length of 3.  
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.  

Example 4:  
Input: s = ""  
Output: 0  

### Solution
Apply _**"Sliding Window"**_ algorithm to this question.  

```Python
class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)

        letter2index = {}
        l = 0
        longest = 0
        for r in range(n):
            if s[r] in letter2index:
                l = max(letter2index[s[r]]+1, l)
            longest = max(longest, r-l+1)
            letter2index[s[r]] = r
        return longest

class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        window = set()
        
        l = 0
        for r in range(len(s)):
            while s[r] in window:
                window.remove(s[l])
                l += 1
            window.add(s[r])
            length = max(length, r-l+1)
        return length
```