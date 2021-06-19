'''
34. Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]
'''

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        return [self.findBound(nums, target, True), self.findBound(nums, target, False)]
    
    def findBound(self, nums, target, lowerBound):
        s, e = 0, len(nums)-1
        while s + 1 < e:
            m = s + (e-s)//2
            if lowerBound:
                if nums[m] >= target:
                    e = m
                else:
                    s = m
            else:
                if nums[m] <= target:
                    s = m
                else:
                    e = m
        first, last = e, s
        if lowerBound:
            first, last = last, first
        if nums[first] == target:
            return first
        if nums[last] == target:
            return last
        return -1