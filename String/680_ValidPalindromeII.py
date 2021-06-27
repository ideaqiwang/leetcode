'''
680. Valid Palindrome II

Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Example 1:
Input: s = "aba"
Output: true

Example 2:
Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.

Example 3:
Input: s = "abc"
Output: false
'''

class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = self.twoPointers(s, 0, len(s)-1)
        if left >= right:
            return True
        
        return self.isPalindrome(s, left+1, right) or self.isPalindrome(s, left, right-1)
        
    def isPalindrome(self, s, l, r):
        left, right = self.twoPointers(s, l, r)
        return left >= right
 
    def twoPointers(self, s, l, r):
        while l < r:
            if s[l].lower() != s[r].lower():
                return l, r
            l += 1
            r -= 1
        return l, r