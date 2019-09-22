'''
  @Description https://leetcode.com/problems/longest-palindromic-substring/
  @IDEA
    Use two pointers to search the longest palidromic substring from middle position to left and right.
'''

class Solution:
    start = 0 # The start index of the longest palindromic substring 
    end = 0   # The end index of the longest palindromic substring

    def longestPalindrome(self, s: str) -> str:
        # Loop through each index of the given string s.
        # For each index, it would be treated as the middle postion.
        # Then expand the palindromic substring. 
        for i in range(len(s)):
          self.findLongest(s, i, i)    # Then length of a palindromic string can be even or odd.
          self.findLongest(s, i, i+1)  # Therefore, we need to search both positions for each index.
        return s[self.start:self.end+1]
        
    def findLongest(self, s, l, r):
      while l>=0 and r<len(s) and s[l]==s[r]:
        l -= 1
        r += 1
      # Compare the current longest palindromic string with the current substring
      # r-l-2 is because l and r would be outside of found palindromic string
      if (self.end-self.start) < (r-l-2):
        self.start = l+1
        self.end = r-1
