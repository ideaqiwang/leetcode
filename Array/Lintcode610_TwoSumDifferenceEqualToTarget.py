'''
610. Two Sum - Difference equals to target

Given an sorted array of integers, find two numbers that their difference equals to a target value.
Return a list with two number like [num1, num2] that the difference of num1 and num2 equals to target value, and num1 is less than num2.

Example 1:
Input: nums = [2, 7, 15, 24], target = 5 
Output: [2, 7] 
Explanation:
(7 - 2 = 5)
'''

class Solution:
    """
    @param nums: an array of Integer
    @param target: an integer
    @return: [num1, num2] (num1 < num2)
    """
    def twoSum7(self, nums, target):
        # write your code here
        n = len(nums)
        target = abs(target)
        j = 1
        for i in range(n):
            j = max(j, i + 1) # nums before j no need to check again
            while j < n and nums[j]-nums[i] < target:
                j += 1
            if j == n:
                break
            if nums[j] - nums[i] == target:
                return [nums[i], nums[j]]
        return None