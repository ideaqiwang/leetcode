'''
28. Implement strStr()

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Clarification:
What should we return when needle is an empty string? This is a great question to ask during an interview.
For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1

Example 3:
Input: haystack = "", needle = ""
Output: 0

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
        lenHaystack, lenNeedle = len(haystack), len(needle)
        if lenHaystack < lenNeedle:
            return -1
        
        i = 0
        while i <= (lenHaystack-lenNeedle):
            matched = True
            for j in range(lenNeedle):
                if haystack[i+j] != needle[j]:
                    matched = False
                    break
            if matched:
                return i
            i += 1
        return -1
