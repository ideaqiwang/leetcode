'''
186. Reverse Words in a String II

Given a character array s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by a single space.
Your code must solve the problem in-place, i.e. without allocating extra space.

Example 1:
Input: s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]

Example 2:
Input: s = ["a"]
Output: ["a"]
'''

class Solution:
    '''
    The idea is reverse the whole list.
    Then reverse each word again.
    '''
    def reverse(self, array, start, end):
        l, r = start, end
        while l < r:
            array[l], array[r] = array[r], array[l]
            l += 1
            r -= 1

    def reverseWords(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if not s:
            return
        n = len(s)
        self.reverse(s, 0, n-1)
        start = end = 0
        while start < n:
            while end < n and s[end] != " ":
                end += 1
            self.reverse(s, start, end-1)
            start = end + 1
            end += 1