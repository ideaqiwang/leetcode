## 1358. Number of Substrings Containing All Three Characters

### Description
Given a string s consisting only of characters a, b and c.

Return the number of substrings containing at least one occurrence of all these characters a, b and c.

Example 1:  
Input: s = "abcabc"  
Output: 10  
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again).  

Example 2:  
Input: s = "aaacb"  
Output: 3  
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb".  

Example 3:  
Input: s = "abc"  
Output: 1  

### Solution
Use **Sliding Window** algorithm.
1. Initialize L, R to 0
2. Outer loop to move R to right and update charCount
3. As long as charCount meets the constraint, move L to right by 1. And update current count.
4. Update the total count.

Time Complexity: O(n)
```python
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        charCount = [0] * 3
        total = current = 0

        l = 0
        for r in range(len(s)):
            charCount[ord(s[r])-ord('a')] += 1
            while l < len(s) and charCount.count(0) == 0:
                charCount[ord(s[l])-ord('a')] -= 1
                l += 1
                current += 1
            total += current
        return total
```
