'''
144 · Interleaving Positive and Negative Numbers

Given an array with positive and negative integers. Re-range it to interleaving with positive and negative integers.

Example 1
Input : [-1, -2, -3, 4, 5, 6]
Outout : [-1, 5, -2, 4, -3, 6]
Explanation :  any other reasonable answer.
'''

class Solution:
    """
    @param: A: An integer array.
    @return: nothing
    """
    def rerange(self, A):
        # Quick select
        numNeg, numPos = 0, 0
        for num in A:
            if num < 0:
                numNeg += 1
            else:
                numPos += 1

        n = len(A)
        def partition(A, startPositive):
            flag = -1 if startPositive else 1
            l, r = 0, len(A)-1
            while l <= r:
                while l <= r and A[l]*flag < 0:
                    l += 1
                while l <= r and A[r]*flag > 0:
                    r -= 1
                if l <= r:
                    A[l], A[r] = A[r], A[l]
                    l += 1
                    r -= 1
        
        def interleave(A, sameLength):
            l, r = 1, n-1
            if sameLength:
                r = n-2
            while l < r:
                A[l], A[r] = A[r], A[l]
                l += 2
                r -= 2
        
        partition(A, numPos > numNeg)
        interleave(A, numPos == numNeg)