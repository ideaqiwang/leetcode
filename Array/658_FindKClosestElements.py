'''
658. Find K Closest Elements

Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.
An integer a is closer to x than an integer b if:
|a - x| < |b - x|, or
|a - x| == |b - x| and a < b
 
Example 1:
Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]

Example 2:
Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]
'''

class Solution:
    '''
    Perform a binary search. At each operation, calculate mid = (left + right) / 2 and
    compare the two elements located at arr[mid] and arr[mid + k]. 
    If the element at arr[mid] is closer to x, then move the right pointer.
    If the element at arr[mid + k] is closer to x, then move the left pointer.
    Remember, the smaller element always wins when there is a tie.
    '''
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        if k == n:
            return arr
        
        l, r = 0, n-k
        while l < r:
            m = l + (r-l)//2
            if x - arr[m] <= arr[m+k] - x:
                r = m
            else:
                l = m+1
        return arr[l:l+k]