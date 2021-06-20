'''
4. Median of Two Sorted Arrays

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Example 3:
Input: nums1 = [0,0], nums2 = [0,0]
Output: 0.00000

Example 4:
Input: nums1 = [], nums2 = [1]
Output: 1.00000
'''

class Solution:
    '''
        Solution 1:
              left_part          |        right_part
        A[0], A[1], ..., A[i-1]  |  A[i], A[i+1], ..., A[m-1]
        B[0], B[1], ..., B[j-1]  |  B[j], B[j+1], ..., B[n-1]
        Find i where:
        1) len(left_part) = len(right_part)
        2) A[i-1] < B[j] and B[j-1] < A[i]
    '''
    def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:
        m, n = len(A), len(B)
        if m > n:
            A, B, m, n = B, A, n, m
        
        l, r, halfLen = 0, m, (m+n+1)//2
        while l <= r:
            i = (l+r) // 2
            j = halfLen - i
            # i is too small. Must increase
            if i < m and B[j-1] > A[i]:
                l = i + 1
            # i is too big. Mush descrease
            elif i > 0 and A[i-1] > B[j]:
                r = i - 1
            else: # Found the perfect i
                maxLeft = 0
                if i == 0:
                    maxLeft = B[j-1]
                elif j == 0:
                    maxLeft = A[i-1]
                else:
                    maxLeft = max(A[i-1], B[j-1])
                
                if (m+n) % 2 == 1:
                    return maxLeft
                
                minRight = 0
                if i == m:
                    minRight = B[j]
                elif j == n:
                    minRight = A[i]
                else:
                    minRight = min(A[i], B[j])
                return (maxLeft+minRight)/2

    '''
    Solution 2:
    Find the kth elememnt from two sorted arrays
    '''
    def findMedianSortedArrays2(self, A: List[int], B: List[int]) -> float:
        m, n = len(A), len(B)
        total = m+n
        if (total) % 2 == 1:
            return self.findKth(A, 0, m-1, B, 0, n-1, (total+1)//2)
        left = self.findKth(A, 0, m-1, B, 0, n-1, total//2)
        right = self.findKth(A, 0, m-1, B, 0, n-1, total//2+1)
        return (left+right) / 2

    def findKth(self, A, startA, endA, B, startB, endB, k):
        lenA, lenB = endA-startA+1, endB-startB+1
        if lenA > lenB:
            return self.findKth(B, startB, endB, A, startA, endA, k)
        
        if lenA == 0:
            return B[startB+k-1]
        if k == 1:
            return min(A[startA], B[startB])
        
        i = startA + min(lenA, k//2)-1
        j = startB + min(lenB, k//2)-1
        if A[i] > B[j]: # B[j+1, j+2, ...] may still have element which less than A[i]
            return self.findKth(A, startA, endA, B, j+1, endB, k-(j-startB+1))
        return self.findKth(A, i+1, endA, B, startB, endB, k-(i-startA+1))
            