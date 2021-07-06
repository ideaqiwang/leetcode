'''
197. Permutation Index

Given a permutation which contains no repeated number, find its index in all the permutations of these numbers, which are ordered in lexicographical order. The index begins at 1.

Example 1:
Input:[1,2,4]
Output:1

Example 2:
Input:[3,2,1]
Output:6
'''

class Solution:
    """
    @param A: An array of integers
    @return: A long integer
    """
    def permutationIndex(self, A):
        # write your code here
        n = len(A)
        total = 0
        factorial = 1
        for i in range(n-1, -1, -1):
            smaller = 0
            for j in range(i+1, n):
                if A[j] < A[i]:
                    smaller += 1
            total += smaller * factorial
            factorial *= n - i
        return total + 1