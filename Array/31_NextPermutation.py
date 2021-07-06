'''
31. Next Permutation

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).
The replacement must be in place and use only constant extra memory.

Example 1:
Input: nums = [1,2,3]
Output: [1,3,2]

Example 2:
Input: nums = [3,2,1]
Output: [1,2,3]
'''

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n < 2:
            return
        
        # Find the first index where nums[index] < nums[index+1]
        index = n-2
        while index >= 0 and nums[index+1] <= nums[index]:
            index -= 1
        
        # Find the first number that is greater than nums[index]
        if index >= 0:
            j = n - 1
            while nums[j] <= nums[index]:
                j -= 1
            nums[index], nums[j] = nums[j], nums[index]
        
        # Reverse all numbers from index+1
        i, j = index+1, n-1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1