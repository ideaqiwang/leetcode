'''
@Description https://leetcode.com/problems/longest-palindrome/
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.
This is case sensitive, for example "Aa" is not considered a palindrome here.

@IDEA
A palindrome string may have two forms. AABB or AACBB
Loop through the given string S, for each letter c, if it's not in the set, add it to the set.
If c is already in the set, which means the 2 same letters can form a palindrome. Therefore, increase length by 2.
And remove the letter from the set. Becase it's been counted.

In the end, if the set is not empty, we can only pick one letter to form a palindrome.
'''
class Solution:
    def longestPalindrome(self, s: str) -> int:
      if not s:
        return 0

      charSet = set() # Create a lookup set
      length = 0
      for c in s:
        # Increase length by 2 and remove it from the set if it's already in it
        if c in charSet:
          length += 2
          charSet.remove(c)
        else:
          # Add c to the set if it doesn't exist
          charSet.add(c)
      # If the set is not empty in the end, we can only select one letter to form the longest palindrome
      if len(charSet) > 0:
        length += 1
      return length
      
