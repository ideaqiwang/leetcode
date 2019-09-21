'''
@Description https://leetcode.com/problems/implement-strstr/

Implement strStr().
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
Return 0 if needle is empty.

@IDEA
Loop through haystack, compare substr and needle.
@Time complexity:
  O(n^2)

@Todo
  A better algorithm is KMP.
'''

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
      if not needle:
        return 0
      if len(needle) > len(haystack):
        return -1
      
      totalLen, wordL = len(haystack), len(needle)
      for i in range(totalLen-wordL+1):
          if haystack[i:i+wordL] == needle:
            return i
      return -1
