'''
302. Smallest Rectangle Enclosing Black Pixels

You are given an image that is represented by a binary matrix with 0 as a white pixel and 1 as a black pixel.
The black pixels are connected (i.e., there is only one black region). Pixels are connected horizontally and vertically.
Given two integers x and y that represent the location of one of the black pixels, return the area of the smallest (axis-aligned) rectangle that encloses all black pixels.

Example 1:
Input: image = [["0","0","1","0"],["0","1","1","0"],["0","1","0","0"]], x = 0, y = 2
Output: 6
'''

class Solution:
    """
    Binary search to find the left, right, top and bottom bounaries of the rectangle which includes all "1".
    """
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        if not image or not image[0]:
            return 0
        m, n = len(image)-1, len(image[0])-1
        l = self.findLeft(image, 0, y)
        r = self.findRight(image, y, n)
        t = self.findTop(image, 0, x)
        b = self.findBottom(image, x, m)
        return (r-l+1) * (b-t+1)

    def findLeft(self, image, s, e):
        while s+1 < e:
            m = (s+e) // 2
            if self.isEmptyColumn(image, m):
                s = m
            else:
                e = m
        if self.isEmptyColumn(image, s):
            return e
        return s
    
    def findRight(self, image, s, e):
        while s+1 < e:
            m = (s+e) // 2
            if self.isEmptyColumn(image, m):
                e = m
            else:
                s = m
        if self.isEmptyColumn(image, e):
            return s
        return e
    
    def findTop(self, image, s, e):
        while s+1 < e:
            m = (s+e) // 2
            if self.isEmptyRow(image, m):
                s = m
            else:
                e = m
        if self.isEmptyRow(image, s):
            return e
        return s
    
    def findBottom(self, image, s, e):
        while s+1 < e:
            m = (s+e) // 2
            if self.isEmptyRow(image, m):
                e = m
            else:
                s = m
        if self.isEmptyRow(image, e):
            return s
        return e
    
    def isEmptyColumn(self, image, col):
        for r in range(len(image)):
            if image[r][col] == "1":
                return False
        return True

    def isEmptyRow(self, image, row):
        for c in range(len(image[0])):
            if image[row][c] == "1":
                return False
        return True