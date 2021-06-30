'''
75. Sort Colors

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.

Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:
Input: nums = [2,0,1]
Output: [0,1,2]

Example 3:
Input: nums = [0]
Output: [0]
'''

class Solution:
    # Quick select with three parts
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, index, r = 0, 0, len(nums)-1
        while index <= r:
            if nums[index] == 0:
                nums[l], nums[index] = nums[index], nums[l]
                l += 1
                index += 1
            elif nums[index] == 2:
                nums[r], nums[index] = nums[index], nums[r]
                r -= 1
            else:
                index += 1