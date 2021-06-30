'''
143. Sort Colors II

Given an array of n objects with k different colors (numbered from 1 to k),
sort them so that objects of the same color are adjacent, with the colors in the order 1, 2, ... k.

Example1
Input: 
[3,2,2,1,4] 
4
Output: 
[1,2,2,3,4]
'''

class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sortColors2(self, colors, k):
        # Quick select
        if not colors:
            return
        self.partition(colors, 1, k, 0, len(colors)-1)

    def partition(self, colors, startColor, endColor, startIdx, endIdx):
        if startColor == endColor or startIdx == endIdx:
            return
        color = (startColor+endColor) // 2
        l, r = startIdx, endIdx
        while l<=r:
            while l <= r and colors[l] <= color:
                l += 1
            while l <= r and colors[r] > color:
                r -= 1
            if l <= r:
                colors[l], colors[r] = colors[r], colors[l]
                l += 1
                r -= 1
        self.partition(colors, startColor, color, startIdx, r)
        self.partition(colors, color+1, endColor, l, endIdx)