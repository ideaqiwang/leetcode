'''
@Description https://leetcode.com/problems/valid-palindrome/
@IDEA
  1. Reconstruct the string which contains alphabet and number.
  2. Use two points(left, right) to check they are the same.
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
      if not s:
        return True
      
      lowerStr = ''
      for c in s:
        if c.isalnum():
          lowerStr += c.lower()
      left, right = 0, len(lowerStr)-1
      
      while left < right:
        if lowerStr[left] != lowerStr[right]:
          return False
        left += 1
        right -= 1
      return True
