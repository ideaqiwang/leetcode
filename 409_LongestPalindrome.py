class Solution:
    def longestPalindrome(self, s: str) -> int:
      if not s:
        return 0

      charSet = set()
      length = 0
      for c in s:
        if c in charSet:
          length += 2
          charSet.remove(c)
        else:
          charSet.add(c)
      if len(charSet) > 0:
        length += 1
      return length
      
