'''
238. Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation. 

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        product = [1]*n
        # Calculate product of all elements to the left of index i
        for i in range(1, n):
            product[i] = product[i-1] * nums[i-1]
        prodFromRight = 1 # the product of all element from i+1 to the right
        for i in range(n-1, -1, -1):
            product[i] *= prodFromRight
            prodFromRight *= nums[i]
        return product